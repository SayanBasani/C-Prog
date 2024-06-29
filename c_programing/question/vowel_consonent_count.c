#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){

    //calculate voewl and consonents
    char name[100];int i,a=0,b=0;
    printf("enter name :- ");
    scanf("%[^\n]",&name);
    int name_len=strlen(name);
    for (i=0;i<name_len;i++){
        if(name[i]!=' '){
            char nam= tolower(name[i]);
            if(nam=='a'||nam=='e'||nam=='i'||nam=='o'||nam=='u'){
                a=a+1;
            }else{
                b=b+1;
            }
        }
        else{
            continue;
        }
    }
    printf("Total %d vowels present in the string \n",a);
    printf("Total %d consonents present in the string ",b);

    return 0;
}