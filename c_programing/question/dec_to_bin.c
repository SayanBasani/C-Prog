#include <stdio.h>

int main(){
    int i,j,k,n,x,a[100];
    printf("enter :-");
    scanf("%d",&x);
    for(i=0;i<x;i++){
        a[i]=x%2;
        x=x/2;
    }
   
    return 0;
}
