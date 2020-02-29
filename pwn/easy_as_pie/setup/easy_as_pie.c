#include <stdio.h>
#include <stdlib.h>

int print_pie(){
    puts("\nHere you go:\n");
    puts("Here you go:\n");
    printf("()()()()()()\n");
	printf("|\\         |\n");
	printf("|.\\. . . . |\n");
	printf("\\'.\\       |\n");
	printf(" \\.:\\ . . .|\n");
	printf("  \\'o\\     |\n");
	printf("   \\.'\\. . |\n");
	printf("    \\\".\\   |   tre\n");
	printf("     \\'`\\ .|\n");
	printf("      \\.'\\ |\n");
	printf("       \\__\\|\n");
	printf("\n");
	return 0;
}

void put_pie(){	
	int (*fpi)();
	fpi = &print_pie;
	//fpi = &exit;
	char get_pie[32] = {0};

	puts("\nGive me your pie: ");			    			        
    read(0, get_pie, 64);
    //scanf("%s", get_pie);
    printf("Got this: %s\n", get_pie);
}

int main(int argc, char** argv){
	setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
	fflush(stdout);

	int menu_option;
	printf("       Even Witchers Need to Eat!!!\n");
    printf("------------------------------------------\n\n");

    do {
	    printf("Main Menu\n");
	    printf("1. Get Pie.\n");
	    printf("2. Put Pie.\n");
	    printf("3. Leave Tavern.\n");
	    printf("Please enter an option from the main menu: ");
	    scanf("%d",&menu_option);

	    switch(menu_option){
		    case 1:
		    	print_pie();
		    	break;
		    case 2:		    	
		    	put_pie();
		    	break;
		    case 3:
		        printf("\nExiting...\n");		        	        
		        exit(0);
		    default:
		        printf("\nInvalid input, try again!");
		        break;
    	} 
    } while(menu_option != 3);
    return 0;
}