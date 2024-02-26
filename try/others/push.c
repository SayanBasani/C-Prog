#include <stdio.h>
#include <stdlib.h>
#define SIZE 4  
int top = -1, arr[SIZE]; 
int push(){
    int x;
            if(top == SIZE-1){
                printf("over flow");
            }else{
                printf("enter number :- ");
                scanf("%d",&x);
                top=top+1;
                arr[top]=x;
            }printf("total element is %d",top+1);
}
void pop(){
    int x;
    if(top == -1){
        printf("under flow ");
    }else{
        printf("%d space of a array and with this %d is pop or deleted",top,arr[top]);
        top=top-1;
    }
}
int show(){
    if(top == -1){
        printf("empty stack");
    }else{
        for(int i=0;i<=top;i++){
            printf("elemrnt %d is :- %d \n",i , arr[i]);
        }
    }
}
int main() {
    printf("This is only for integers .");
    int cho;
    while(1){
        printf(" \nWhat you want to perfom : -");
        printf("\n1.for push\n2.for pop\n3.for show all element\n4.for end \n :-");
        scanf("%d",&cho);
        if(cho==1){
            push();
        }
        if(cho == 2){
            pop();
        }
        if(cho == 3){
            show();
        }
        if(cho==4){
            printf("Exit");
            break;
        }
    }
}