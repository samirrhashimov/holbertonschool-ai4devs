import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def line(status, size="512", method="GET", path="/index.html"):
    return (f'127.0.0.1 - frank [10/Oct/2023:13:55:36 -0700] '
            f'"{method} {path} HTTP/1.1" {status} {size}')


@pytest.fixture
def analyzer():
    return LogAnalyzer()


def test_parse_valid_common_line(analyzer):
    r = analyzer.parse_line(line(200))
    assert r == {
        "ip": "127.0.0.1", "timestamp": "10/Oct/2023:13:55:36 -0700",
        "method": "GET", "path": "/index.html", "protocol": "HTTP/1.1",
        "status": 200, "bytes": 512,
    }


def test_parse_combined_format_with_extras(analyzer):
    s = line(404) + ' "http://ref.example/" "Mozilla/5.0"'
    r = analyzer.parse_line(s)
    assert r["status"] == 404 and r["path"] == "/index.html"


def test_parse_dash_bytes_is_zero(analyzer):
    assert analyzer.parse_line(line(304, size="-"))["bytes"] == 0


def test_parse_post_method_and_query_path(analyzer):
    r = analyzer.parse_line(line(201, method="POST", path="/api?x=1"))
    assert r["method"] == "POST" and r["path"] == "/api?x=1"


def test_parse_malformed_returns_none(analyzer):
    assert analyzer.parse_line("this is not a log line") is None


def test_parse_empty_line_returns_none(analyzer):
    assert analyzer.parse_line("") is None


def test_parse_surrounding_whitespace_ok(analyzer):
    assert analyzer.parse_line("  " + line(200) + "\n")["status"] == 200


def test_analyze_empty_list(analyzer):
    r = analyzer.analyze([])
    assert r["total_requests"] == 0
    assert r["error_rate"] == 0.0
    assert r["status_counts"] == {}


def test_analyze_no_errors(analyzer):
    r = analyzer.analyze([line(200), line(301), line(204)])
    assert r["total_requests"] == 3
    assert r["error_requests"] == 0
    assert r["error_rate"] == 0.0


def test_analyze_all_errors(analyzer):
    r = analyzer.analyze([line(404), line(500), line(503)])
    assert r["error_rate"] == 100.0


def test_analyze_boundary_399_vs_400(analyzer):
    r = analyzer.analyze([line(399), line(400)])
    assert r["error_requests"] == 1
    assert r["error_rate"] == 50.0


def test_analyze_rounding_two_decimals(analyzer):
    r = analyzer.analyze([line(500), line(200), line(200)])
    assert r["error_rate"] == 33.33


def test_analyze_skips_malformed_lines(analyzer):
    r = analyzer.analyze([line(200), "garbage", line(500)])
    assert r["total_requests"] == 2
    assert r["malformed_lines"] == 1
    assert r["error_rate"] == 50.0


def test_analyze_status_counts(analyzer):
    r = analyzer.analyze([line(200), line(200), line(404), line(500)])
    assert r["status_counts"] == {200: 2, 404: 1, 500: 1}


def test_analyze_only_malformed_lines(analyzer):
    r = analyzer.analyze(["bad", "worse"])
    assert r["total_requests"] == 0
    assert r["malformed_lines"] == 2
    assert r["error_rate"] == 0.0