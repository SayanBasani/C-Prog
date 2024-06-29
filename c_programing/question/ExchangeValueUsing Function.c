#include <stdio.h>
void sayan(int *a,int *b){
    int c=*a;
    *a=*b;
    *b=c;
}
int main(){
    int a=5;int b=6;
    printf("%d   %d ",a,b);
    sayan(&a,&b);
    printf("%d  %d",a,b);
    return 0;
}