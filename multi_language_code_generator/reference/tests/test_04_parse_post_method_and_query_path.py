import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def line(status, size="512", method="GET", path="/index.html"):
    return (f'127.0.0.1 - frank [10/Oct/2023:13:55:36 -0700] '
            f'"{method} {path} HTTP/1.1" {status} {size}')


def test_parse_post_method_and_query_path():
    analyzer = LogAnalyzer()
    r = analyzer.parse_line(line(201, method="POST", path="/api?x=1"))
    assert r["method"] == "POST" and r["path"] == "/api?x=1"