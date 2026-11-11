import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def line(status, size="512", method="GET", path="/index.html"):
    return (f'127.0.0.1 - frank [10/Oct/2023:13:55:36 -0700] '
            f'"{method} {path} HTTP/1.1" {status} {size}')


def test_analyze_skips_malformed_lines():
    analyzer = LogAnalyzer()
    r = analyzer.analyze([line(200), "garbage", line(500)])
    assert r["total_requests"] == 2
    assert r["malformed_lines"] == 1
    assert r["error_rate"] == 50.0