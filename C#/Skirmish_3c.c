// Create a C project in CodeGrade using the provided template I3L2Sk3c.c

// Write a program that prompts the user for 2 integer values and stores them in variables.

// You will also need variables for sum, difference, product and quotient.

// Use the increment operator to add 1 to the first value.
// Use the decrement operator to subtract 1 from the second value.
// Note: You don't need to display the new values after increment/decrement but the new
// values will be used in the calculations.
// Calculate the sum of the 2 values and store in variable.
// Calculate the difference of the 2 values (subtract the second value from the first value) and store in variable.
// Calculate the product of the 2 values and store in variable.
// Calculate the quotient of the 2 values (dividing the first number by the second number) and store in variable.
// Output should include full sentences to include answers (Ex...Sum of the 2 numbers is ##)
// Note: Each variable should be declared on a separate line.
// Note: Include comments throughout the program to tell what the code does

#include <stdio.h>
int main(){

int x;//empty variable for value #1
int y;//empty variable for value #2


printf("\nInput your first number:");//request user input for both vairables
scanf("\n%d", &x);
printf("\nInput your second number:");
scanf("\n%d", &y);

x++;//increments first variable
y--;//decrements second variable

printf("\n Sum of the 2 values is %d", x+y);//Adds the two values
printf("\n Difference of the 2 values is %d", x-y); //Subtracts the two values
printf("\n Product of the 2 numbers is %d", x*y); //Multiplys the two values
printf("\n Quotient of the 2 numbers is %d", x/y); //Divides the two values

	return 0;
}