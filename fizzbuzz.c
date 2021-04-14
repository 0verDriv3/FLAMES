/*
	Title  : Fizz Buzz
	Author : Diamond Rivero
	Date   : 04/14/2021
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argv, char** argc) {
	int fb_number;

	printf("Fizz Buzz: \n");
	printf("Enter a number: ");
	scanf("%d", &fb_number);

	for(int index = 1; index < (fb_number - 1); index++) {
		if (index % 3 == 0 && index % 5 == 0)
		{
			printf("[%d]: FizzBuzz\n", index);
		} else if(index % 3 == 0) {
			printf("[%d]: Fizz\n", index);
		} else if(index % 5 == 0) {
			printf("[%d]: Buzz\n", index);
		} else {
			printf("[%d]: Ineligible\n", index);
		}
	}

	return 0;
}