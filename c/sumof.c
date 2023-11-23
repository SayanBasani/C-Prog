#include <stdio.h>
#include <conio.h>
int main() {
     float a,b,c=0,d=1;
     printf("enter any number");
     scanf("%f",&a);
     for(b=1;b<=a;b++)
     {
          d=d*b;
          c=c+(b/d);
     }
          printf("%f\n",c);
}