async function fetchUserData(userId) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ id: userId, username: "alex_dev" });
        }, 100);
    });
}

function generateWelcomeMessage(userId) {
    const user = fetchUserData(userId);
    const message = `Welcome back, ${user.username}!`;
    return message;
}

console.log(generateWelcomeMessage(101));