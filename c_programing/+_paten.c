#include <stdio.h>

int main(){

    int i,j,k,y,z,x;
    printf("enter any number :- ");
    scanf("%d",&x);
    int h=x/2;
    // printf("%d\n",h);
    for(i=0;i<x;i++){
        
        if(i==h){
            for(j=0;j<x;j++){
            if(j==x-1){
                printf("* \n");
            }else{
                printf("*");
            }
            }
        }else{
        for(z=0;z<h;z++){
            printf(" ");
        }
        printf("* \n");
            
            
       }
    }

    return 0;
}