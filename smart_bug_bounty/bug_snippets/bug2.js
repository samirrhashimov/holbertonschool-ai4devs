async function fetchUserData(userId) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ id: userId, username: "alex_dev" });
        }, 100);
    });
}

function generateWelcomeMessage(userId) {
    // Bug: Missing await inside async workflow
    const user = fetchUserData(userId); 
    
    // Bug: Prints "[object Promise]" instead of actual username
    const message = `Welcome back, ${user.username}!`;
    return message;
}

console.log(generateWelcomeMessage(101));