//identify prime no. using swetch statement
#include<stdio.h>
#include<conio.h>
int main() {
     int a,b;
    printf("enter a number");
    scanf("%d",&a);
    b=a%2;
    switch (b) 
    {
    case 1:
        printf("it is a prime number");
        break;
    case 0:
        printf("it is a not-prime number");
        break;
    default:
        printf("no ans");
        break;
    }
}