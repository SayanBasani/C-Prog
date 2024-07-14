#include <stdio.h>
//*    *
// * *
//  *
// * *
//*   *

int main(){
    int i,j,x,b,c;
    scanf("%d",&x);
    b=c=x;
    printf("%d  %d  %d \n",x,b,c);
    for(i=1;i<=x-1;i++){
        for(j=1;j<=x;j++){
            if(j==i||j==x-i)printf("*");
            else printf(" ");
            
        }
        printf("\n");
        
    }
    

    

    return 0;
}