#include <stdio.h>
#include<conio.h>

int main(){

    int a[2][3],b[2][3],c[3][3],r1,c1,r2,c2,i,j;
    printf("enter 1");
    scanf("%d %d",& r1 ,& c1);
    printf("enter 2");
    scanf("%d %d",& r2 , & c2);
    if(r1==r2 && c1==c2)
    {
        printf("matrix addition possiable");
        printf("enter nos 1st matrix no's");
    for(i=0;i<3;i++)
    for(j=0;j<3;j++)
// 2   for(j=0;j<3;j++)
    scanf("%d", & a[i][j]);
    
    printf("enter nos 2nd matrix no's");
    for(i=0;i<r2;i++)
    for(j=0;j<c2;j++)
    scanf("%d", & b[i][j]);

    for(i=0;i<r1;i++)
    for(j=0;j<c2;j++)
        // scanf("%d",a[i][j]+b[i][j]);
    c[i][j]=a[i][j]+b[i][j];
    printf("display result in matrix form");

    for(i=0;i<r1;i++)
    {
    for(j=0;j<c2;j++)
    printf("%d",a[i][j]);
    printf("\n");
    }
    }
    else
    printf("addition is not possiable");
    
    return 0;
}