#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* create_greeting(const char* name) {
    if (name == NULL) return NULL;

    size_t length = strlen("Hello, ") + strlen(name) + 2;
    char* message = (char*) malloc(length);
    
    if (message == NULL) {
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
        free(greeting);
    }

    return 0;
}