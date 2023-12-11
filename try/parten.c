#include <stdio.h>

int main(){

    int i,j,k,l,m,x=4;
    // for(i=0;i<x;i++){
    //     for(j=x;j>0;j--){
    //         if(j+i==x){
    //             printf("*");
    //         }else printf(" ");
    //     }
    //     printf("\n");
    // }
    for(j=x-1;j>=-1;j--){
        for(i=0;i<x;i++){
            if(j<i){
                printf("*");
            }else
            {
                printf(" ");
            }
            
        }
        printf("\n");
    }

    return 0;
}