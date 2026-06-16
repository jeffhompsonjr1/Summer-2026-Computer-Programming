#include <stdio.h>

int main(){



//conditional operator
//experssion ? if true:if false

// x > y ? printf("x is bigger"): printf("y is bigger");

// z < y ? printf("\ny is bigger"): printf("\nz is bigger");


// int choice;
// float drinkPrice;
// printf("Drinks\n");
// printf("Iced Tea .......$2.50\n");
// printf("Soda .......$3.00\n");
// printf(" Please choose a drink (Iced Tea (1) or Soda (2))");
// scanf("%d", &choice);
// drinkPrice = (choice ==1 ? 2.50 : 3.00 );
// printf("%f", drinkPrice);

// int a = 2, b = 6, result;

// result = b/a + b + b * 2;
// printf("\n%d", result);

// result = a - b;
// printf("\n%d", result);

// result = a / b;
// printf("\n%d", result);

// result = a * b;
// printf("\n%d", resu


int y; // Holds an empty integer to take the users input

int x;


printf("Enter any number   "); //prints the statement for the user
scanf("%d", &y); // User input

x = y % 2; //computes input for x

printf("%d",y);
printf("%d", x);
x == 0 ? printf("Even"):printf("Odd"); // compares y vs x, if y is greater than x the statement prints positive, else the statement is negative.

	return 0;
}

