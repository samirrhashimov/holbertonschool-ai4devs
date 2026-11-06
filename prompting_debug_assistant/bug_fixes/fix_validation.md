# Fix Validation Log

## Bug 1 – bug1_fixed.py
- **Input**: [1, 2, 3, 4, 5], n=3
- **Expected Output**: [3, 4, 5]
- **Actual Output**: [3, 4, 5] ✅
- **Notes**: Negative indexing fixed off-by-one error.

## Bug 2 – bug2_fixed.js
- **Input**: cart = [{ price: 1000, quantity: 1 }, { price: 25, quantity: 2 }], discount = 10
- **Expected Output**: 960.00
- **Actual Output**: 960.00 ✅
- **Notes**: Formatted with `.toFixed(2)` at string output stage.

## Bug 3 – bug3_fixed.c
- **Input**: create_greeting("Alice")
- **Expected Output**: Hello, Alice!
- **Actual Output**: Hello, Alice! ✅
- **Notes**: Memory dynamically allocated with `malloc()` and released with `free()`.

## Bug 4 – bug4_fixed.py
- **Input**: {"users": []}
- **Expected Output**: 0.0
- **Actual Output**: 0.0 ✅
- **Notes**: Defensive checks prevent ZeroDivisionError.

## Bug 5 – bug5_fixed.js
- **Input**: orders = [{ id: 101 }, { id: 102 }, { id: 103 }]
- **Expected Output**: Processing order #101, #102, #103, total: 3
- **Actual Output**: Processing order #101, #102, #103, total: 3 ✅
- **Notes**: Replaced `var` with `let` and handled sequence with `async/await`.