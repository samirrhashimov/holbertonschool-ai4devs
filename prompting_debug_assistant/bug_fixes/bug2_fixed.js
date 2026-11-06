function calculateCartTotal(cartItems, discountPercentage) {
    let total = 0;
    
    cartItems.forEach(item => {
        total += item.price * item.quantity;
    });

    if (discountPercentage > 0) {
        let discount = total * (discountPercentage / 100);
        total = total - discount;
    }

    return total;
}

const cart = [
    { name: "Laptop", price: 1000, quantity: 1 },
    { name: "Mouse", price: 25, quantity: 2 }
];

let finalTotal = calculateCartTotal(cart, 10);
let totalWithShipping = finalTotal + 15.00;

console.log(`Final Total: $${totalWithShipping.toFixed(2)}`);