async function processOrders(orders) {
    let completedCount = 0;
    
    for (let i = 0; i < orders.length; i++) {
        await new Promise(resolve => setTimeout(resolve, 100));
        console.log("Processing order #" + orders[i].id);
        completedCount++;
    }
    
    return completedCount;
}

const orders = [{ id: 101 }, { id: 102 }, { id: 103 }];

processOrders(orders).then(result => {
    console.log("Completed orders recorded:", result);
    if (result === 3) {
        console.log("bug5_fixed.js: Async execution passed successfully! ✅");
    } else {
        console.error("bug5_fixed.js: Test failed! ❌");
    }
});