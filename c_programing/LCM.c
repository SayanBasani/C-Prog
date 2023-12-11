#include <stdio.h>
int main()
{
    int a,b,i,c,d,e,j;
    printf("enter any 2 number");
    scanf("%d",&a);
    scanf("%d",&b);
    e=0;
    
        c=a;  d=b;
    for (i=1;i<=b; i++)
    {
        if (c%i)
        {
            /* code */
        }
        
    }
    
    
    for(i=1;i<=b;i++)
    {
        if (a%i==0)
        {
            for(j=1; j <= i; j++)
            {
                if (b%j==0)
                {
                    if (i==j)
                    {
                        e=i;
                    }
                    
                }
                
            }
            
        }
        
    }
    printf("%d",e);
    return 0;
}