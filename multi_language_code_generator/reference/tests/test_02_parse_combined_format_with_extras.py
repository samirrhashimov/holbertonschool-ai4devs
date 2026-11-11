import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def line(status, size="512", method="GET", path="/index.html"):
    return (f'127.0.0.1 - frank [10/Oct/2023:13:55:36 -0700] '
            f'"{method} {path} HTTP/1.1" {status} {size}')


def test_parse_combined_format_with_extras():
    analyzer = LogAnalyzer()
    s = line(404) + ' "http://ref.example/" "Mozilla/5.0"'
    r = analyzer.parse_line(s)
    assert r["status"] == 404 and r["path"] == "/index.html"