/*
1. Write a program to push elements in a empty stack.
2. Write a program to pop element from a stack.
3. Write a program to insert an element to a queue.
4. Write a program to delete an element from a queue.
5. Write a program to insert an element to a single link list.
6. Write a program to delete an element from a single link list from any position.
7. Write a program to insert an element to a doubly link list.
8. Write a program to delete an element from a doubly link list from any position.
*/
/*
9. Write a program to find out factorial of a number using recursion
*/
// Write a program to push elements in a empty stack.
/*#include <stdio.h>
#define max  4
int top = -1;
int arr[max];
int main(){
    while(1){
        if(top==max-1){
            printf("Over flow condiation.\n");
            break;
        }else{
            int a;
            printf("enter number for push :-\n");
            scanf("%d",&a);
            top=top+1;
            arr[top]=a;
            // printf("present numbers are :-");
            int i;
            printf("exesting numbers are :- \n");
            for(i=0;i<=top;i++){
                printf("  %d  ",arr[i]);
            }printf("\n");
        }
    }}*/
// Write a program to pop element from a stack.
// #include <stdio.h>
// #define max 4
// int top = -1;
// int arr[max];
// int main()
// {
//     while (1)
//     {
//         printf("\n1.To push\n2.to pop \n3.to Exit\n");
//         int x,i;
//         scanf("%d", &x);
//         if (x == 1)
//         {
//             if (top == max - 1)
//             {
//                 printf("over flow condiation \n\n\n");
//             }
//             else
//             {
//                 printf("enter element :-");
//                 scanf("%d", &x);
//                 top = top + 1;
//                 arr[top] = x;
//                 printf("exesting valus :- ");
//                 for(i=0;i<=top;i++){
//                     printf("  %d  ",arr[i]);
//                 }
//             }
//         }
//         else if (x == 2)
//         {
//             if (top == -1)
//             {
//                 printf("under flow \n\n\n");
//             }
//             else
//             {
//                 top = top - 1;
//                 printf("exesting valus :- ");
//                 for(i=0;i<=top;i++){
//                     printf("  %d  ",arr[i]);
//                 }
//             }
//         }
//         else if (x == 3)
//         {
//             break;
//         }
//         else
//         {
//             printf("erong entry. retry..");
//         }
//     }
// }
//Write a program to insert an element to a queue.
// Write a program to delete an element from a queue.
// #include <stdio.h>
// #define max 4
// int arr[max];
// int fornt=0,rear=-1,count;
// int main (){
//     while(1){
//     int x,i;
//     printf("\n1.for add element\n2.for remove element\n3.for exit \n");
//     scanf("%d",&x);
//     if (x==1){
//         if(rear==max-1){
//             printf("The Queue is full.\n");
//         }else{
//             printf("enter element :- \n");
//             scanf("%d",&x);
//             rear=rear+1;
//             arr[rear]=x;
//             printf("elements are :- ");
//             for(i=fornt;i<=rear;i++){
//                 printf("  %d  ",arr[i]);
//             }
//         }
//     }else if(x==2){
//         if(rear+1==fornt){
//             printf("under flow\n");
//         }else{
//             fornt =fornt +1;
//             printf("elements are :- ");
//             for(i=fornt;i<=rear;i++){
//                 printf("  %d  ",arr[i]);
//             }
//         }
//     }else if(x==3){
//         break;
//     }else{
//         printf("Wrong entry . try again...\n");
//     }
// }}

// Write a program to insert an element to a queue.
/*
#include <stdio.h>
#define max 4
int arr[max];
int fornt=0,rear=-1,count;
int main (){
    while(1){
    int x,i;
    // if (x==1){
        if(rear==max-1){
            printf("The Queue is full.\n");
            break;
        }else{
            printf("enter element :- \n");
            scanf("%d",&x);
            rear=rear+1;
            arr[rear]=x;
            printf("elements are :- ");
            for(i=fornt;i<=rear;i++){
                printf("  %d  ",arr[i]);
            }printf("\n");
        // }
    }}}
    */
//     else if(x==2){
//         if(rear==fornt){
//             printf("under flow\n");
//         }else{
//             fornt =fornt +1;
//             printf("elements are :- ");
//             for(i=fornt;i<=rear;i++){
//                 printf("  %d  ",arr[i]);
//             }
//         }
//     }else if(x==3){
//         break;
//     }else{
//         printf("Wrong entry . try again...\n");
//     }
// }}


// Write a program to insert an element to a single link list.
#include<stdio.h>  
#include<stdlib.h>  
void beginsert(int);  
struct node  
{  
    int data;  
    struct node *next;  
};  
struct node *head;  
void main ()  
{  
    int choice,item;  
    do   
    {  
        printf("\nEnter the item which you want to insert?\n");  
        scanf("%d",&item);  
        beginsert(item);  
        printf("\nPress 0 to insert more ?\n");  
        scanf("%d",&choice);  
    }while(choice == 0);  
}  
void beginsert(int item)  
    {  
        struct node *ptr = (struct node *)malloc(sizeof(struct node *));  
        if(ptr == NULL)  
          {  
            printf("\nOVERFLOW\n");  
        }  
        else  
        {  
            ptr->data = item;  
            ptr->next = head;  
            head = ptr;  
            printf("\nNode inserted\n");  
        }  
          
    }  