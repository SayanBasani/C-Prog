#include<stdio.h>
int main() {
    int a,b,c,i;
    printf("enter 1st and 2nd no :-");
    scanf("%d\n%d",&a,b);
    printf("enter 1 :- sum   , 2 :- substraction  , 3 :- multeplaction , 4 :- devision");
    scanf("%d",&i);
    switch(c)   
    {
    case 1:
        c=a+b;
        printf("%d",c);
        break;
    case 2:
        c=a-b;
        printf("%d",c);
        break;
    case 3:
        c=a*b;
        printf("%d",c);
        break;
    case 4:
        c=a/b;
        printf("%d",c);
        default:
        break;
    }
}