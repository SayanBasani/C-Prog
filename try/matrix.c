// odd and even deferencate and average between range
#include<stdio.h>

int main() {
    double a,b,c=0,i,d=0,s1=0,s2=0;
    
    printf("enter range");
    scanf("%lf , %lf \n",&a , &b);
    for(i=a;i<=b;i++)
    {
    if(i%2==0)
        {
            s1=s1+i;
            c=c+1;
        }
    else
        {
            s2=s2+i;
            d=d+1;
        }
    }
    printf(" even average :- %lf \n ",(s1/c));
    printf("odd average :- %lf",(s2/d));
}
