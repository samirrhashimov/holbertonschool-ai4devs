"""Reference implementation of LogAnalyzer (Python baseline).

Specification (shared by all language ports)
--------------------------------------------
parse_line(line) -> dict | None
    Parses one Apache Common/Combined Log Format line:
      IP IDENT USER [TIMESTAMP] "METHOD PATH PROTOCOL" STATUS BYTES [extras]
    Returns {"ip", "timestamp", "method", "path", "protocol", "status", "bytes"}
    status is int; bytes is int ("-" -> 0). Returns None for malformed lines.

analyze(lines) -> dict
    total_requests : number of VALID lines
    error_requests : valid lines with status >= 400
    error_rate     : error_requests / total_requests * 100, rounded to 2
                     decimals; 0.0 when total_requests == 0
    malformed_lines: number of lines that could not be parsed
    status_counts  : {status_code: count} for valid lines
"""
import re
from typing import Optional

_LOG_PATTERN = re.compile(
    r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) ([^"]+)" (\d{3}) (\d+|-)(?: .*)?$'
)


class LogAnalyzer:
    def parse_line(self, line: str) -> Optional[dict]:
        match = _LOG_PATTERN.match(line.strip())
        if not match:
            return None
        ip, timestamp, method, path, protocol, status, size = match.groups()
        return {
            "ip": ip,
            "timestamp": timestamp,
            "method": method,
            "path": path,
            "protocol": protocol,
            "status": int(status),
            "bytes": 0 if size == "-" else int(size),
        }

    def analyze(self, lines: list) -> dict:
        total = 0
        errors = 0
        malformed = 0
        status_counts: dict = {}

        for line in lines:
            entry = self.parse_line(line)
            if entry is None:
                malformed += 1
                continue
            total += 1
            status = entry["status"]
            status_counts[status] = status_counts.get(status, 0) + 1
            if status >= 400:
                errors += 1

        error_rate = round(errors / total * 100, 2) if total else 0.0
        return {
            "total_requests": total,
            "error_requests": errors,
            "error_rate": error_rate,
            "malformed_lines": malformed,
            "status_counts": status_counts,
        }