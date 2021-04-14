/*
	Title  : Table Generator
	Author : Diamond Rivero
	Date   : 04/14/2021
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argv, char** argc) {
	int width;
	int height;

	printf("Table Generator: \n");
	printf("Enter Width: ");
	scanf("%d", &width);
	printf("Enter Height: ");
	scanf("%d", &height);

	for(int i = 0; i < height; i++) {
		for(int j = 0; j < width; j++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}