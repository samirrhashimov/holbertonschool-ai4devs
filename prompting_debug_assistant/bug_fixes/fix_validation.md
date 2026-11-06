# Bug Fix Validation Log

## Bug 1 – bug1_fixed.py
- **Input**: `items = [10, 20, 30, 40, 50], n = 2`
- **Expected Output**: `[40, 50]`
- **Actual Output**: `[40, 50]` ✅
- **Edge Case Input**: `items = [10, 20, 30, 40, 50], n = 5`
- **Expected Output**: `[10, 20, 30, 40, 50]`
- **Actual Output**: `[10, 20, 30, 40, 50]` ✅
- **Notes**: AI's negative slicing approach (`items[-n:]`) resolved the off-by-one error completely.

---

## Bug 2 – bug2_fixed.js
- **Input**: `cart = [{ price: 1000, quantity: 1 }, { price: 25, quantity: 2 }], discount = 10`
- **Expected Output**: `960.00`
- **Actual Output**: `960.00` ✅
- **Notes**: Moving `.toFixed(2)` to the final presentation string prevented implicit string concatenation.

---

## Bug 3 – bug3_fixed.c
- **Input**: `create_greeting("Alice")`
- **Expected Output**: `Hello, Alice!`
- **Actual Output**: `Hello, Alice!` ✅
- **Notes**: Replaced stack-allocated local array with dynamic heap allocation using `malloc()` and added `free()` in `main()`.

---

## Bug 4 – bug4_fixed.py
- **Input**: `{"users": []}`
- **Expected Output**: `0.0` (No DivisionByZero error)
- **Actual Output**: `0.0` ✅
- **Notes**: Added defensive zero-length checks before calculating average score.

---

## Bug 5 – bug5_fixed.js
- **Input**: `orders = [{ id: 101 }, { id: 102 }, { id: 103 }]`
- **Expected Output**: Logs order IDs sequentially and returns total completed count `3`.
- **Actual Output**: Logs `101`, `102`, `103` and returns `3` ✅
- **Notes**: Switched from `var` to block-scoped `let` and refactored loop with `async/await`.