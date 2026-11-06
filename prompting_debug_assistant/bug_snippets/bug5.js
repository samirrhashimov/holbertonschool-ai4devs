function processOrders(orders) {
    let completedCount = 0;
    
    for (var i = 0; i < orders.length; i++) {
        setTimeout(function() {
            console.log("Processing order #" + orders[i].id);
            completedCount++;
        }, 100);
    }
    
    return completedCount;
}

const orders = [{ id: 101 }, { id: 102 }, { id: 103 }];
const result = processOrders(orders);
console.log("Completed orders recorded:", result);