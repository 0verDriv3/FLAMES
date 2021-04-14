/*
	Title  : Guessing Game
	Author : Diamond Rivero
	Date   : 04/14/2021
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int exitGame = 1;

int main(int argv, char** argc) {
	while(exitGame) {
		srand(time(NULL)); // seed a random number generator
		int guessNum = 0, guessLimit = 0, tries = 0;
		int secretNumber = 0;
		char option;

		// Set the game level.
		while(1) {
			printf("E - Easy mode[1-10]\nI - Intermediate Mode[1-20]\nH - Hard mode[1-30]\n");
			printf("Set Level: ");
			scanf("%s", &option);

			if (option == 'E' || option == 'e') {
				secretNumber = rand() % 10 + 1; // generate between 1 to 10 numbers
				guessLimit = 10;
				break;
			} else if(option == 'I' || option == 'i') {
				secretNumber = rand() % 20 + 1; // generate between 1 to 20 numbers
				guessLimit = 5;
				break;
			} else if(option == 'H' || option == 'h') {
				secretNumber =  rand() % 30 + 1; // generate between 1 to 30 numbers
				guessLimit = 3;
				break;
			} else {
				printf("Invalid input, try again.\n");
			}

		} 

		// Guessing Game Core.
		while(guessNum != secretNumber && guessLimit > 0) {
			printf("Enter your guess[%d]: ", guessLimit);
			scanf("%d", &guessNum);

			if(guessNum == secretNumber) {
				printf("Correct!\n");
				tries++;
				break;
			} else if(guessNum > secretNumber) {
				printf("Your guess is too high.\n");
				guessLimit--;
				tries++;
			} else if(guessNum < secretNumber) {
				printf("Your guess is too low.\n");
				guessLimit--;
				tries++;
			} else {
				printf("Invalid Input!");
			}
		}

		// Number of guesses and the exit game validation.
		if(guessNum == secretNumber) {
			printf("Number of tries: %d.\n", tries);
			printf("Do you want to try again?[Yes/No]: ");
			scanf("%s", &option);

			switch(option) {
				case 'Y':
				case 'y':
					continue;
				case 'N':
				case 'n':
					break;
				default:
					printf("Invalid input, exiting...\n");
					break;
			}

			exitGame = 0;

		} else {
			printf("%d Guess, failed.\n", guessLimit);
			printf("Do you want to try again?[Yes/No]: ");
			scanf("%s", &option);

			switch(option) {
				case 'Y':
				case 'y':
					continue;
				case 'N':
				case 'n':
					break;
				default:
					printf("Invalid input, exiting...\n");
					break;
			}

			exitGame = 0;

		}
	}

	return 0;
}
