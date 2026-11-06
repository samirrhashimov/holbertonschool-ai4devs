function calculateCartTotal(cartItems, discountPercentage) {
    let total = 0;
    
    cartItems.forEach(item => {
        total += item.price * item.quantity;
    });

    if (discountPercentage > 0) {
        let discount = total * (discountPercentage / 100);
        total = total - discount;
    }

    // Keep total as a primitive number during calculation
    return total;
}

const cart = [
    { name: "Laptop", price: 1000, quantity: 1 },
    { name: "Mouse", price: 25, quantity: 2 }
];

let finalTotal = calculateCartTotal(cart, 10);
let totalWithShipping = finalTotal + 15.00;

// Format to 2 decimal places only at the final presentation step
console.log(`Final Total: $${totalWithShipping.toFixed(2)}`);

// Assertion / Validation
if (totalWithShipping.toFixed(2) === "960.00") {
    console.log("bug2_fixed.js: Test passed successfully! ✅");
} else {
    console.error("bug2_fixed.js: Test failed! ❌");
}