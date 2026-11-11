# Risk Assessment Matrix

| Risk | Severity | Notes |
| --- | --- | --- |
| Hardcoded Credentials & Secrets | High | API keys and database passwords are stored directly in static configuration files. |
| Deprecated Hashing Algorithms | High | User authentication relies on unsalted MD5 hashes, creating severe security vulnerabilities. |
| Missing Automated Tests | High | Zero unit or integration test coverage makes system updates highly risky. |
| Synchronous Blocking Operations | Medium | Heavy image processing runs on the main thread, leading to request timeouts. |
| High Module Coupling | Medium | Monolithic scripts tightly combine API calls, business logic, and database access. |
| Lack of Diagnostic Logging | Low | Exceptions are caught silently without audit logs, making debugging difficult. |