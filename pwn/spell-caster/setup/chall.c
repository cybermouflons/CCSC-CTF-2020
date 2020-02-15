#include <stdio.h>

#define FLAGSIZE 64

char location[] = "Circle_Of_Elements";

void get_flag()
{
    char buf[FLAGSIZE];
    FILE *f = fopen("flag.txt","r");
    if (f == NULL) {
        printf("Flag File is Missing. Problem is Misconfigured\n");
        exit(0);
    }
    fgets(buf,FLAGSIZE,f);
    printf(buf);
}

int main(int argc, char *argv[])
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char *spells[] = {"Aard\n", "Igni\n", "Yrden\n", "Quen\n", "Axii\n"};
    printf("Witcher Spells:\n================\n");
    int spell_cnt = sizeof(spells) / sizeof(*spells);
    for (char **p = spells; p < spells + spell_cnt; ++p) {
        printf("- %s", *p);
    }

    printf("\nChoose spell to cast: ");
    char buf[80];
    fgets(buf, sizeof(buf), stdin);

    for(int i = 0; i < spell_cnt; ++i) {
        if(!strcmp(spells[i], buf)) {
            printf("\n>>>> Casting: %s", buf);
            return 0;
        }
    }

    char msg[100];
    snprintf(msg, sizeof(msg), "Spell not found : %s\n", buf);
    printf(msg);

    for(int i=0; location[i]!='\0'; i++) {
        if(location[i] != "Circle_Of_Elements"[i]) { 
            puts("You are not in the Circle of Elements! You can't cast any spells!\n"); 
        }
    }

    return 0;
}
