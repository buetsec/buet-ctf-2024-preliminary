#include <stdio.h>
#include <stdlib.h>

void play(float *balance);
void withdraw(float *balance);
void checkBalance(float balance);
void checkFlag(float *balance);

int main()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    float balance = 0.0;
    int choice;

    printf("=== Welcome to Guesser ===\n");

    while (1)
    {
        printf("\nChoose an option:\n");
        printf("1. Play game\n");
        printf("2. Withdraw money\n");
        printf("3. Check balance\n");
        printf("4. Check Flag\n");
        printf("5. Exit\n");
        printf("Enter your choice: \n");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            play(&balance);
            break;
        case 2:
            withdraw(&balance);
            break;
        case 3:
            checkBalance(balance);
            break;
        case 4:
            if (balance < 10000)
            {
                printf("You need to have at least $10000 to check the flag.\n");
                exit(0);
            }
            checkFlag(&balance);
            break;
        case 5:
            printf("Exiting the program. Thank you for playing!\n");
            exit(0);
        default:
            printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}

void play(float *balance)
{
    if (*balance < 1)
    {
        printf("You need at least $1 to play the game.\n");
        exit(0);
    }
    *balance -= 1;
    printf("Guess a random number between 1 and 10: \n");
    int guess;
    scanf("%d", &guess);
    int random = rand() % 10 + 1;
    if (guess == random)
    {
        *balance += 10;
        printf("Congratulations! You have won $10. Your new balance is $%.2f.\n", *balance);
    }
    else
    {
        printf("Sorry, you have lost. The correct number was %d. Your new balance is $%.2f.\n", random, *balance);
    }
}

void withdraw(float *balance)
{
    float amount;
    printf("Enter the amount to withdraw: $\n");
    scanf("%f", &amount);

    if (abs(amount) > 10)
    {
        printf("You can only withdraw $10 at a time.\n");
        exit(0);
    }
    *balance -= amount;
    printf("You have successfully withdrawn $%.2f. Your new balance is $%.2f.\n", amount, *balance);
}

void checkBalance(float balance)
{
    printf("Your current balance is: $%.2f\n", balance);
}

void checkFlag(float *balance)
{
    FILE *fptr;
    char c;
    fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        printf("Error! flag.txt file not found.\n");
        exit(1);
    }
    printf("Flag: ");
    while ((c = fgetc(fptr)) != EOF)
    {
        printf("%c", c);
    }
    fclose(fptr);
    printf("\n");
}