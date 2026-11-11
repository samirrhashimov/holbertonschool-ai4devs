# Bug Descriptions

## bug1.py
- **Language**: Python
- **Intended Behavior**: Calculate the average grade of students from a list of scores, ignoring any negative scores.
- **Current Issue**: ZeroDivisionError occurs when all scores in the list are negative or the list is empty, and an off-by-one error excludes valid zero scores.

## bug2.js
- **Language**: JavaScript
- **Intended Behavior**: Asynchronously fetch user profile data and construct a user greeting message.
- **Current Issue**: Missing `await` keyword on an asynchronous function call, resulting in `[object Promise]` string concatenation instead of resolved data.

## bug3.java
- **Language**: Java
- **Intended Behavior**: Check if a given string is a palindrome by comparing characters from both ends.
- **Current Issue**: String comparison uses `==` operator instead of `.equals()`, and index out-of-bounds occurs due to incorrect loop condition `i <= str.length()`.

## bug4.py
- **Language**: Python
- **Intended Behavior**: Maintain a dynamic default list of tags across multiple call invocations to tag system objects.
- **Current Issue**: Uses a mutable default argument (`tags=[]`), causing state persistence across unrelated function calls.