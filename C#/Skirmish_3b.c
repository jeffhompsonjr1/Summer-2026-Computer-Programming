// Create a C project in CodeGrade using the provided template I3L2Sk3b.c

// Write a program that prompts the user for 3 float values and stores them in variables. 

// Using logical operators, relational operators and a conditional ternary operator to display the largest number. 
// If the user enters      1.2     2.3     3.4
// Display should be "The largest number is 3.4".
// If all 3 numbers are the same display "All numbers are equal.".
// Note: Each variable should be declared on a separate line.
// Note: Include comments throughout the program to tell what the code does

#include <stdio.h>

int main()
{
	
float x;// Empty variables for the 3 user inputs
float y;
float z;
float l; //empty variable to store the largest value

printf("Enter Number #1 \n");// User prompt
scanf("%f", &x);
printf("Enter Number #2 \n");// User prompt
scanf("%f", &y);
printf("Enter Number #3 \n");// User prompt
scanf("%f", &z);	

(x > y && x > z) ? l = x : l != x; //solve for x
(y > x && y > z) ? l = y : l != y; //solve for y
(z > y && z > x) ? l = z : l != z; //solve for z
(x == y && x == z) ? printf("All numbers are equal.") : printf("The largest number is %.1f", l); 

	return 0;
}