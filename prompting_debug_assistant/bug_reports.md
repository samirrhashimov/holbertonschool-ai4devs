# Structured Bug Reports (`bug_reports.md`)

This document provides formal technical bug reports for each identified defect in the project. Each section details the issue summary, root cause analysis, resolution steps (distinguishing AI-generated suggestions from manual edits), and key takeaways.

---

## Bug Report – bug1.py

- **File Name**: `bug1.py`
- **Bug Summary**: Off-by-one indexing error in list slicing logic.
- **Root Cause**: The calculation `start_index = len(items) - n + 1` shifts the starting index one element too far to the right. When `n == len(items)`, the starting index evaluates to `1`, omitting the first list element entirely.
- **Resolution**: 
  - *AI Suggestion*: Replace manual index arithmetic with Python's idiomatic negative slice syntax (`items[-n:]`).
  - *Manual Edits*: Added defensive guard clauses (`if not items or n <= 0: return []`) and inline unit assertions for edge case validation.
- **Lessons Learned**: Prefer built-in language idioms (like Python negative slicing) over manual index arithmetic to eliminate off-by-one errors. Always test edge cases where `n` equals array length or zero.

---

## Bug Report – bug2.js

- **File Name**: `bug2.js`
- **Bug Summary**: Implicit string concatenation leading to incorrect total calculations.
- **Root Cause**: The function `calculateCartTotal` returned `total.toFixed(2)`, which returns a primitive `string` rather than a `number`. Adding `15.00` to this string performed string concatenation (e.g., `"945.00" + 15.00 = "945.0015"`).
- **Resolution**: 
  - *AI Suggestion*: Keep numeric values as primitive numbers throughout calculations and apply `.toFixed(2)` only at display time.
  - *Manual Edits*: Refactored the calculation function to return primitive floats and formatted the string output directly inside `console.log`.
- **Lessons Learned**: Avoid converting numerical data to formatted display strings mid-pipeline. Keep mathematical operations strictly numeric until final presentation rendering.

---

## Bug Report – bug3.c

- **File Name**: `bug3.c`
- **Bug Summary**: Memory management failure resulting in a dangling pointer and undefined behavior.
- **Root Cause**: `create_greeting` allocated string memory on the local stack frame (`char message[50]`). When the function returned, its stack frame popped, invalidating the returned pointer and causing memory access errors in caller code.
- **Resolution**: 
  - *AI Suggestion*: Dynamically allocate string memory on the heap using `malloc()` with `strlen()` calculations.
  - *Manual Edits*: Added explicit null checks for `malloc` return values and inserted `free(greeting);` in `main()` to prevent memory leaks.
- **Lessons Learned**: Never return pointers to local stack-allocated variables in C/C++. Use dynamic heap allocation (`malloc`/`free`) or caller-allocated buffers for returned pointers.

---

## Bug Report – bug4.py

- **File Name**: `bug4.py`
- **Bug Summary**: Unhandled runtime exceptions (`ZeroDivisionError` and missing dictionary keys).
- **Root Cause**: The function attempted to divide `total_score` by `valid_users` without validating if `valid_users > 0`. An empty input dataset resulted in a runtime zero-division crash.
- **Resolution**: 
  - *AI Suggestion*: Use a guard condition (`if not users: return 0.0`) and safe key retrieval with `.get()`.
  - *Manual Edits*: Wrapped file reading in `try-except` blocks to handle missing or corrupted JSON files gracefully.
- **Lessons Learned**: Always implement defensive checks for dynamic data inputs (such as external JSON payloads) before performing mathematical division or dictionary indexing.

---

## Bug Report – bug5.js

- **File Name**: `bug5.js`
- **Bug Summary**: Asynchronous scope closure error and invalid return timing.
- **Root Cause**: Using `var` inside a loop created a single shared function-scoped variable `i`. By the time `setTimeout` callbacks executed asynchronously, `i` had reached `orders.length` (out-of-bounds). Additionally, the function returned synchronously before callbacks completed.
- **Resolution**: 
  - *AI Suggestion*: Change `var` to block-scoped `let` and refactor the loop using `async/await` with Promises.
  - *Manual Edits*: Structured the function signature with `async` and updated test calls to handle the returned Promise via `.then()`.
- **Lessons Learned**: Never use `var` inside asynchronous loops; use `let` to bind variable state per iteration. Use Promises and `async/await` when waiting for asynchronous tasks to complete.