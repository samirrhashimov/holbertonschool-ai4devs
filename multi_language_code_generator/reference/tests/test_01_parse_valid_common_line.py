import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def line(status, size="512", method="GET", path="/index.html"):
    return (f'127.0.0.1 - frank [10/Oct/2023:13:55:36 -0700] '
            f'"{method} {path} HTTP/1.1" {status} {size}')


def test_parse_valid_common_line():
    analyzer = LogAnalyzer()
    r = analyzer.parse_line(line(200))
    assert r == {
        "ip": "127.0.0.1", "timestamp": "10/Oct/2023:13:55:36 -0700",
        "method": "GET", "path": "/index.html", "protocol": "HTTP/1.1",
        "status": 200, "bytes": 512,
    }