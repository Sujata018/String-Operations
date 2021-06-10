#include<stdio.h>
#include<string.h>
#include<stdlib.h>

/*
Usage : <pgmname> <string> <stretching-factor>

This program takes a string and a stretching factor as command line argument, and prints the string stretched by the factor.

E.g. Input : StringStretch.c Hawk 5
     Output: HHHHHaaaaawwwwwkkkkk
*/

int main(int argc, char *argv[])
{
	if (argc !=3){								//Check if 3 arguments are passed
		printf("Usage : <pgmname> <string> <stretching-factor>" );
		return 1;
	}
	
	int lenStr,i=0,j=0,k=0,factor;

	lenStr=strlen(argv[1]);							// First argument is the string to be stretched
	factor = atoi(argv[2]);							// Second argument is the factor by which the string is to be stretched
	
	if (factor < 1) {
		printf("Stretching factor is not a positive whole number" );
		return 1;
	}
	
	char result[lenStr*factor+1];						// Set length of stretched string =  lenth of string * stretch factor. Additional 1 bit for null character. 
	for (;i<lenStr;i++){							// Stretch each character to stretching factor 
		for (k=0;k<factor;k++){
			result[j++]=argv[1][i];	
		}
	}
	result[j]='\0';								// Add null character at the end 
	printf("%s", result);							// Print the result
	return 0;
}
