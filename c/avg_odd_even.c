#include<stdio.h>
#include <math.h>

int main()
{
    int a,b,i,j,x=0,y=0,u=0,v=0;
    printf("enter range ");
    scanf("%d , %d",&a,&b);
    for(i=a;i<=b;i++)
    {
    if(i%2==0)
{
    x=x+i;
    // v=v+1;
}
    else
{
    y=y+i;
    // u=u+1;
}
    }
    // int aa,bb;
    // aa=x/v;
    // bb=y/u;
    // printf("even %d  odd  %d",aa,bb);
    printf(" %d",x);
    printf(" %d",y);
    

    return 0;
}