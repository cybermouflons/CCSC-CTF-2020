#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void get_flag() {
    FILE * fp;
    fp = fopen ("flag.txt", "r");
    char flag[256];
    fscanf(fp, "%s", flag);
    printf("%s\n", flag);

    fclose(fp);
}

struct user_struct {
    void (*getMail)();
    char username[32];
};

struct user_struct * user = NULL;
char * message;
char line[128];

int handle_login() {
    printf("username > ");
    fflush(stdout);
    if (fgets(line, sizeof(line), stdin) == NULL) {
        return 0;
    }
    user = malloc(sizeof(struct user_struct));
    memset(user, 0, sizeof(user));
    if (strlen(line) <= 31) {
        strcpy(user->username, line);
    } else {
        printf("Invalid username\n");
        fflush(stdout);
        free(user);
        user = NULL;
    }
    return 1;
}

void check_email() {
    if (user != NULL) {
        if (user->getMail != NULL) {
            user->getMail();
        } else {
            printf("You appear to have no mail.\n");
        }
    } else {
        printf("You need to login first\n");
    }
}

int leave_message() {
    if (message != NULL) { 
        free(message);
        message = NULL;
    }
    printf("message > ");
    fflush(stdout);
    if (fgets(line, sizeof(line), stdin) == NULL) {
        return 0;
    }
    message = strdup(line);
    return 1;
}

int main() {
    int running = 1;

    printf("\n-_-_-_-_-_-_-_-_-_-_-_-\n");
    printf(" Kaer Morheny\n");
    printf("-_-_-_-_-_-_-_-_-_-_-_-\n\n");
    
    
    while (running) {
        printf("\n1. login\n");
        printf("2. logout\n");
        printf("3. check email\n");
        printf("4. leave message\n");
        printf("5. disconnect\n\n");

        printf("> ");
        fflush(stdout);

        if (fgets(line, sizeof(line), stdin) == NULL) {
            break;
        }

        if (line[0] == '1') {
            if (handle_login() == 0) {
                break;
            }
        } else if (line[0] == '2') {
            free(user);
        } else if (line[0] == '3') {
            check_email();
        } else if (line[0] == '4') {
            if (leave_message() == 0) {
                break;
            }
        } else if (line[0] == '5') {
            running = 0;
            printf("logging out...\n");
        } else {
            printf("\nInvalid option.\n\n");
        }
    }


    return 0;
}