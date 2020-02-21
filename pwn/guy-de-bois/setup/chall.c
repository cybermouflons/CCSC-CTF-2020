#include<stdio.h>
#include<string.h>

void gadget() {
    asm("jmp *%rsp");
}

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char buf[100];
    printf("Guillaume: Witcher! I've a prime urgency and import! I must speak to you!\n");
    scanf("%s",buf);
    printf("Witcher: %s.\n",buf);
    return 0;
}