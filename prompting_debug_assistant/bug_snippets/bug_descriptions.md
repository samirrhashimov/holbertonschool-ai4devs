# Bug Descriptions & Intended Behaviors

## Bug 1 – bug1.py
**Intended Behavior**: Slice and return the last `n` items of a list.  
**Issue Type**: Off-by-one / Slice indexing error.  
**Notes**: The function computes `start_index = len(items) - n + 1`, which skips the first element of the requested slice. When `n == len(items)`, it misses the head element entirely.

---

## Bug 2 – bug2.js
**Intended Behavior**: Compute the discounted total of items in a shopping cart and add a flat shipping rate.  
**Issue Type**: Type conversion / Misuse of library method (`Number.prototype.toFixed()`).  
**Notes**: `total.toFixed(2)` returns a `string`, not a `number`. Adding `15.00` to the result performs string concatenation instead of numeric addition (e.g., `"945.0015"` instead of `960.00`).

---

## Bug 3 – bug3.c
**Intended Behavior**: Dynamically construct and return a formatted greeting string for a given name.  
**Issue Type**: Memory management / Dangling pointer (Undefined Behavior).  
**Notes**: `message` is allocated on the stack inside `create_greeting`. Returning a pointer to a local stack array results in dangling reference access once the function frame pops.

---

## Bug 4 – bug4.py
**Intended Behavior**: Read user JSON data from a file, calculate, and return the average score across users.  
**Issue Type**: Runtime Exception (`ZeroDivisionError` & unhandled `KeyError`).  
**Notes**: If the `users` list is empty, `valid_users` remains `0`, causing a `ZeroDivisionError` at runtime. Additionally, missing expected keys in dictionary objects are unhandled.

---

## Bug 5 – bug5.js
**Intended Behavior**: Asynchronously process a list of orders and print each order ID upon completion.  
**Issue Type**: Scope closure error (`var` binding in loop) & Asynchronous timing issue.  
**Notes**: Using `var` inside a `for` loop shares a single function-scoped `i` variable across closure callbacks in `setTimeout`, causing `orders[i]` to evaluate to `undefined` out-of-bounds. Furthermore, returning `completedCount` synchronously returns `0` before asynchronous timeouts fire.