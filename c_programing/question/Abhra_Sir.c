#include<string.h>
#include<stdio.h>
#include<ctype.h>
int main() {
    char s[10][10],t[10];
    int i,j,n;
    printf("Enter how many name you wante to enter :- ");
    scanf("%d",&n);
    printf("Enter names :- ");

    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d",j);
            scanf("%s",&s[i][j]);
        }}
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(strcpy(s[j],s[j+1])>0){
                strcpy(t,s[j]);
                strcpy(s[j],s[j+1]);
                strcpy(s[j+1],t);
            }
        }
    }
    printf("Alphabatic order :- ");
    for(i=0;i<n;i++){
        puts(s[i]);
    }
}