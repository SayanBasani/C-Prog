#include<stdio.h>
int main(){
    int a=1;
    int b=1;
    for(a=1;a<=3;a++){
        printf("index %d\n",a);
        b=b*5;
        printf("%d\n",b);
    }
}