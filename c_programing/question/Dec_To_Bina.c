#include <stdio.h>
int main() {
    int i,j,k,num,a[10];
    num=10;
    j=num;
    for(i=0;i<=num;i++){
        a[i]=num%2;
        num=num/2;
    }
    for(i=j;i=0;i--){
        if(i==0 || i==1){
            printf("%d",a[i]);
        }
    }
}