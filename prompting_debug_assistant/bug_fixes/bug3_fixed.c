#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Dynamically allocates heap memory to create a greeting string.
 * Caller is responsible for freeing the returned memory.
 */
char* create_greeting(const char* name) {
    if (name == NULL) return NULL;

    // Calculate required buffer length: "Hello, " + name + "!" + '\0'
    size_t length = strlen("Hello, ") + strlen(name) + 2;
    char* message = (char*) malloc(length);
    
    if (message == NULL) {
        perror("Failed to allocate memory");
        return NULL;
    }

    strcpy(message, "Hello, ");
    strcat(message, name);
    strcat(message, "!");
    
    return message;
}

int main() {
    char* greeting = create_greeting("Alice");
    
    if (greeting != NULL) {
        printf("%s\n", greeting);
        
        // Free dynamically allocated heap memory to prevent memory leak
        free(greeting);
        greeting = NULL;
        printf("bug3_fixed.c: Memory freed successfully and test passed! ✅\n");
    } else {
        printf("bug3_fixed.c: Failed to generate greeting! ❌\n");
        return 1;
    }

    return 0;
}