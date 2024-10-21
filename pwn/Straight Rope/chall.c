#include<stdio.h>
#include<stdlib.h>

void win(int a, int b)
{
    if(a!=0xdadababa){
        exit(0);
    }
    if(b!=0xbabadada){
        exit(0);
    }
    FILE* f = fopen("flag.txt","r");
    if(f==NULL){
        printf("flag.txt not found\n");
        exit(0);
    }
    char flag[50];
    fgets(flag, 50, f);
    printf("%s\n",flag);
    fclose(f);
}

void setup()
{
    char buffer[100];
    gets(buffer);
    printf("%s\n",buffer);
}

int main()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setup();
    return 0;
}