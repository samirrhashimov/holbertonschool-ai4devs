#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* create_greeting(const char* name) {
    char message[50];
    strcpy(message, "Hello, ");
    strcat(message, name);
    strcat(message, "!");
    return message;
}

int main() {
    char* greeting = create_greeting("Alice");
    printf("%s\n", greeting);
    return 0;
}