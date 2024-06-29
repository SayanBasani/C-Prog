#include <stdio.h>
#include <math.h> 
#include <string.h>
// make power 
int po(int n,int p){
    int i,j=1;
    for (i=1;i<=p;i++){
        j=j*n;
        // printf("%d",j);
    }
    return j;
}
// number to bionery
int bio(int n){
    int i,j=0,k=0,ans,l=1;
    while(n){
        i=n%2;
        j=j+i*l;
        l=l*10;
        n=n/2;
    }
    return j;
}
// bionery to number
int dec(int num){
    int i,j=0,n=0;
    while(num!=0){
        i=num%10;
        if(i==1){
            int p = po(2,j);
            n=n+p;
        }
        j++;
        num=num/10;
    }
    return n;
}
//text to bionery
int call1(){
    printf("enter the text :- ");
    char te[1000];
    scanf("%s",te);
    for (int i=0 ;i<strlen(te);i++){
        int j=te[i];
        printf("%d ",bio(j));
    }
}
// bionery to text converter
int call2(){
    printf("enter bionery code(mainten the spaces) : -");
    long bi;
    int a,n,i;
    scanf("%lb",&bi);
    // for()
    while(bi!=0){
        
    }
}
int main() {
    printf("%d \n",bio(97));
    printf("%d",dec(101));
    printf("1. text to bionery\n2.bionery to text");
    int comm;
    scanf("%d",&comm);
    if(comm==1){
        call1();
    }else if(comm ==2){
        call2();
    }
    // dec('a');
    // int b='a';
    // printf("%d  %d %d",'a',b,dec(b));
}