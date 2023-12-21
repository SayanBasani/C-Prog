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
    char a[10][10];
    int i,j;
    

    for ( i = 0; i < 2; i++)
    {
        printf("enter name :- ");
        scanf("%s",&a[i]);
    }
    
    for ( i = 0; i < 2; i++)
    {
        printf("%s",a[i]);
        // scanf("%s",&a[i]);
    }
    

    return 0;
}
