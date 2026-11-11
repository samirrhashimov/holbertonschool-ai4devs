## Section 1 - ImageProcessor::process_raw_frame()
- **Plain English**: Takes raw camera pixel arrays, applies manual brightness adjustments, and crops face regions using hardcoded pixel coordinate boundaries.
- **Pattern**: Deeply nested procedural loops with direct array element manipulation.
- **Issues**: High computational complexity, blocks the main thread, and completely lacks exception handling for invalid image shapes.
- **Improvements**: Replace manual pixel iterations with vectorized NumPy operations or OpenCV routines and offload frame processing to an asynchronous task queue.

## Section 2 - UserAuth::validate_legacy_token()
- **Plain English**: Checks user session validity by hashing input parameters with a hardcoded static salt string and querying a legacy database table.
- **Pattern**: Inline SQL query string concatenation inside a procedural validation function.
- **Issues**: Vulnerable to SQL injection, relies on deprecated MD5 hashing algorithms, and lacks token expiration checks.
- **Improvements**: Replace with standard JWT authentication using secure modern cryptographic libraries and parameterized ORM queries.

## Section 3 - FaceDetector::cascade_fallback()
- **Plain English**: Attempts to detect faces using an old OpenCV Haar Cascade classifier whenever the primary neural network fails or times out.
- **Pattern**: Bare try-except block catching all generic exceptions without logging or retry limits.
- **Issues**: Silently suppresses errors, causing CPU utilization to spike when fallback fails repeatedly in a loop.
- **Improvements**: Implement explicit timeout handling, log error details properly, and replace Haar Cascade with a lightweight ONNX runtime model.

## Section 4 - DatabaseManager::fetch_all_photos()
- **Plain English**: Queries all historic photo records from the MySQL database in a single query and loads every row into memory as a list of dictionaries.
- **Pattern**: Unconstrained SELECT query execution.
- **Issues**: Creates severe memory leaks when handling datasets with thousands of records, causing high response latency.
- **Improvements**: Implement SQL pagination using LIMIT and OFFSET and select only required column attributes.