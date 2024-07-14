// #include <stdio.h>
// #include <string.h>
// #include<ctype.h>

// int main(){
//     // make a discanery
//     char a[10];int i,j,b;
//     printf("enter how mach name you want to store :- ");
//     scanf("%c",&b);
//     for (i=0;i<b;i++){
//         printf("enter names :- ");
//         scanf("%s",&)
//     }
    

//     return 0;
// }
#include <stdio.h>
#include <string.h>
#include<ctype.h>

int main(){
    // make a discanery
    char a[10][10],t[10];
    int i,j;
    

    for ( i = 0; i < 2; i++)
    {
        printf("enter name :- ");
        scanf("%s",&a[i]);
    }
    
    // for ( i = 0; i < 2; i++)
    // {
    //     printf("%s  ",a[i]);
    //     // scanf("%s",&a[i]);
    // }

    // printf("%d , %d ",a[0][0], a[0][0+1]);
    // if(a[0][0]>a[0][0+1]){
    //     printf("  yes ");
    //      }

    for(i=0;i<2;i++){
        printf(" a %d  ",i); 
        for(j=0;j<2;j++){
            printf("b %d",j);
            if(a[i][j]>a[i][j+1]){
                // t=" ";
                // strcpy(t,a[j]);
                // strcpy(a[j],a[j+1]);
                // strcpy(a[j+1],t);
                printf("%s ",a[i][j]);
            }
        }
    }printf("it is complit ");
    printf("Alphabatic order :- ");
    for(i=0;i<2;i++){
        // for(j=0;j<2;j++){
            printf("%S",a[i]);
        
    }

    return 0;
}			
