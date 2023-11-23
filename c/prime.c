// identify prime no. using if else statement
#include <stdio.h>
#include <conio.h>
int main()
{
    int a, b;
    printf("enter a namber");
    scanf("%d", &a);
    b = a % 2;
    // printf("%d",b);
    if (b == 1)
    {
        printf("this is a prime number");
    }
    else
    {
        printf("this is a non-prime number");
    }
}