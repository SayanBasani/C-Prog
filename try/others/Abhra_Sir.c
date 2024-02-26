#include <string.h>
#include <stdio.h>
#include <ctype.h>
int main()
{
    char s[10][10], *t;
    int i, j, n;
    printf("Enter how many name you wante to enter :- ");
    scanf("%d", &n);
    printf("Enter names :- ");

    for (i = 0; i < n; i++)
    {
        printf("%d \n enter name :- ", j);
        scanf("%s", &s[i]);
    }

    for (i = 0; i < n-1; i++)
    {
        if (s[i] > s[i + 1])
        {
            strcpy( t , s[i]);
            strcpy(s[i] , s[i + 1]);
            strcpy(s[i + 1] , t);
        }
    }

printf("Alphabatic order :- \n ");
for (i = 0; i < n; i++)
{
    printf(" %s \n ", s[i]);
}
}
// if('abc'>'cba'){
//     printf("%d",'a');
//     // printf("sayan");
// }else{
//     printf("%d",'cba');
// printf("bab");

// printf("%d - %d - %d - %d \n  ",'abc','a','b','c');
// printf("%d - %d - %d - %d",'cba','c','b','a');
// printf("%d   .",'ZZZ');
// printf("%d",'zzz');

