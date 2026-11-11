# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items of a list.
- **Current Issue**: Off-by-one error due to incorrect slicing (`-n + 1`).

## bug2.js
- **Intended Behavior**: Return the average of the numbers in an array.
- **Current Issue**: The loop uses `<=` instead of `<`, so it reads `undefined` and the result becomes `NaN`.

## bug3.java
- **Intended Behavior**: Return true when the entered password equals the stored password.
- **Current Issue**: Uses `==` to compare strings (reference comparison) instead of `.equals()`.

## bug4.py
- **Intended Behavior**: Return only the user whose username matches the input.
- **Current Issue**: SQL injection vulnerability because the query is built by string concatenation instead of parameterized queries.