# Fix Validation

## bug1.py
- **Original Issue**: Off-by-one error, slice `items[-n + 1:]` dropped an element.
- **Fix Applied**: Changed the slice to `items[-n:]`.
- **Test Results**: All 3 test cases passed
  - `([1,2,3,4,5], 3)` -> `[3, 4, 5]`
  - `([1,2,3], 0)` -> `[]`
  - `([1,2], 5)` -> `[1, 2]`

## bug2.js
- **Original Issue**: Loop condition `i <= numbers.length` read `undefined`, so the result was `NaN`.
- **Fix Applied**: Changed to `i < numbers.length` and added an empty-array guard.
- **Test Results**: All 3 test cases passed
  - `[80, 90, 70, 100]` -> `85`
  - `[10]` -> `10`
  - `[]` -> `0`

## bug3.java
- **Original Issue**: `==` compared string references, so equal passwords were rejected.
- **Fix Applied**: Replaced `==` with `Objects.equals(input, stored)`.
- **Test Results**: All 3 test cases passed
  - `new String("secret123")` vs `"secret123"` -> `true`
  - `"wrong"` vs `"secret123"` -> `false`
  - `null` vs `"secret123"` -> `false` (no exception)

## bug4.py
- **Original Issue**: SQL injection through string concatenation in the query.
- **Fix Applied**: Used a parameterized query (`WHERE username = ?`).
- **Test Results**: All 3 test cases passed
  - `"alice"` -> `[(1, 'alice')]`
  - `"bob"` -> `[(2, 'bob')]`
  - `"' OR '1'='1"` -> `[]` (injection blocked)