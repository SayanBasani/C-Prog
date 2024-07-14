// // write a program to find gcd (gratest common factor) for 2 number
// #include <stdio.h>
// int main() {
//     int num1 , num2 ,i,j;
//     printf("Enter two number :- \n");
//     scanf("%d \n ",&num1);
//     scanf("%d \n ",&num2);
//     for (i=1;i<=num1;i++){
//         if(num1%i==0 && num2%i==0){
//             j=i;
//         }
//         printf("%d \n",i);
//     }
//     printf("%d \n",j);
//     printf("compit");
// }

// check a number is devide by 5 and 11 
// #include <stdio.h>
// int main() {
//     printf("Enter numner to check :- ");
//     int num , i ;
//     scanf(" %d ",& num);
//     if(num%5 == 0 && num%11 == 0){
//         printf("\n %d is devide by 5 and 11 ", num);
//     }
// }

// write a proram to check gread pointage and grade in c

// #include <stdio.h>

// float per(float n){
//     return (n*100)/70;
// }
// char gd(int n){
//     // char gd ;
//     if (n>=90){
//         return 'A';
//     }else if(n>=80){
//         return 'B';
//     }else if(n>=70){
//         return 'C';
//     }else if(n>=60){
//         return 'D';
//     }else if(n>=40){
//         return 'E';
//     }else if(n<=40){
//         return 'F';
//     }
// }

// int main(){

//     printf("enter numbers of 5 subject (c, py , ds,algo,cso)-- \n ");
//     float c, py , ds,algo,cso;

//     scanf(" %f \n %f \n%f \n%f \n%f \n",& c ,& py ,& ds , & algo ,& cso);
//     printf("your percentege in c :- %f '%%  Grade point is :-  %c \n ",per(c) , gd(per(c)));
//     printf("your percentege in py :- %f '%%  Grade point is :-  %c\n ",per(py), gd(per(py)));
//     printf("your percentege in ds :- %f '%%  Grade point is :-  %c\n ",per(ds), gd(per(ds)));
//     printf("your percentege in algo :- %f '%%  Grade point is :-  %c\n ",per(algo), gd(per(algo)));
//     printf("your percentege in cso :- %f  '%%  Grade point is :- %c \n ",per(cso), gd(per(cso)));

//     return 0;
// }



// //  Write a C program to compute the average of n random even numbers.
// #include <stdio.h>
// int main() {
//     int num[300],i,n;
//     float add=0;
//     printf("enter how much number you want to compute :- ");
//     scanf("%d",&n);
//     printf("enter numbers");
//     for(i=0;i<n;i++){
//         scanf("%d",&num[i]);
//     }
//     for(i=0;i<n;i++){
//         printf(" %d number is %d \n",i,num[i]);
//         add=add+num[i];
//     }
//     printf("Average if all number is %f ",add/n);
// }

// // 3.	Write a C program to calculate the sum of digits of a number.

// #include <stdio.h>
// int main() {
//     int num,i=0,j;
//     printf("Enter any number :- ");
//     scanf("%d",&num);
//     while(num != 0){
//         i=i+num%10;
//         num=num/10;
//     }
//     printf("%d",i);
// }

// // 4.	Write a C program to calculate the factorial of a number
//  #include <stdio.h>
//  int main() {
//     printf("enter number to calculate factorial :- ");
//     int num,i,j=1;
//     scanf("%d",&num);
//     while(num != 0){
//         printf("%d \n ",num);
//         j=j*num;
//         num=num-1;
//     }
//     printf("answer :- %d",j);
//  }

// // 5.	Write a C program to find the largest element of an array.
// #include<stdio.h>
// int main() {
//     int arr[5],i,j=0,n;
//     printf("enter number of element :- ");
//     scanf("%d",& n);
//     for(i=0;i<n;i++){
//         scanf("%d  ",& arr[i]);
//     }
//     for(i=0;i<n;i++){
//         if(arr[i]>j){
//             j=arr[i];
//         }
//     }
//     printf("largest element is :-  %d",j);
// }

// // 6.	Write a C program to calculate the sum of diagonal elements of a matrix.
// #include <stdio.h>

// int main(){

//     int a[10][10],r,c,i,j,k;
//     printf("enter row and colume number how mach you want : -");
//     scanf("%d  ",&r);
//     scanf("%d  ",&c);
//     for (i=0;i<r;i++){
//         for(j=0;j<c;j++){
//             printf("index (%d,%d):- ",i,j);
//             scanf("%d",&a[i][j]);
//             printf("\n");
//         }
//     }
//     for (i=0;i<r;i++){
//         for(j=0;j<c;j++){
//             // printf("index (%d,%d):- ",i,j);
//             printf("  %d  ",a[i][j]);
//         }
//         printf(" \n ");
//     }
//     k=0;
//     if(c==r){
//         for (i=0;i<r;i++){
//             for(j=0;j<c;j++){
//                 if(i==j){
//                     k=k+a[i][i];
//                 }
//         }}
//         printf("k = %d",k);
//     }else{
//         printf("it is not possiable");
//     }

//     return 0;
// }

// // 7.	Write a C program to compute the numbers  of vowels in a given string.
// #include <stdio.h>
// #include<string.h>

// int main(){

//     char a[100];
//     int i,j;
//     printf("Enter any word :- ");
//     scanf("%s",&a);
//     printf("Your string length id :- %d",strlen(a));

//     return 0;
// }

// // 8.	Write a C program to print the reverse of a string.
// #include <stdio.h>
// #include<string.h>
// int main(){
//     char a[100],b[100];
//     int i,j=0,n;
//     printf("enter any word :- ");
//     scanf("%s",&a);
//     n=strlen(a);
//     j=n;
//     for(i=0;i<n;i++){
//         --j;
//         b[i]=a[j];
//         printf("%d \n %c = %c \n",i,b[i],a[j]);
//     }
//     printf(" ans :- %s",b);
//     return 0;
// }

// // 9.	Write a C program to find the sum of the series 1+(1+2)+(1+2+3)+ ……..upto n terms .
// #include<stdio.h>
// int main() {
//     printf("Enter number :- ");
//     int n,i,j,k,l=0;
//     scanf("%d",&n);
//     for (i=1;i<=n;i++){
//         k=0;
//         for(j=1;j<=i;j++){
//             k=k+j;
//         }
//         l=l+k;
//     }
//     printf("Answer :- %d",l);
// }

// // 10.	Write a C program to calculate GCD of two numbers.
// #include <stdio.h>
// int main() {
//     printf("Enter two number for gcd :- ");
//     int num1,num2,i,j;
//     scanf("%d   %d",& num1,& num2);
//     for(i=1;i<=num1;i++){
//         if(num1%i==0&&num2%i==0){
//             j=i;
//         }
//     }
//     printf("Answer :- %d",j);
// }

// // 11.	Write a C program for addition of two matrices.

// #include<stdio.h>
// int main() {
//     int a[3][3],b[3][3],i,j,c[3][3];
//     printf("Enter 1st matrix :- ");
//     for(i=0;i<3;i++){
//         for(j=0;j<3;j++){
//             printf("Index %d,%d :- ",i+1,j+1);scanf("%d",&a[i][j]);
//         }
//     }
//     printf("Enter 2nd matrix :- ");
//     for(i=0;i<3;i++){
//         for(j=0;j<3;j++){
//             printf("Index %d,%d :- ",i+1,j+1);scanf("%d",&b[i][j]);
//         }
//     }
//     printf("Your matri are \n first matrix :- \n");
//     for(i=0;i<3;i++){
//         for(j=0;j<3;j++){
//             printf("  %d  ",a[i][j]);
//         }
//         printf("\n");
//     }
//     printf("\n first matrix :- \n");
//     for(i=0;i<3;i++){
//         for(j=0;j<3;j++){
//             printf("  %d  ",b[i][j]);
//         }
//         printf("\n");
//     }
//     for(i=0;i<3;i++){
//         for(j=0;j<3;j++){
//             c[i][j]=a[i][j]+b[i][j];
//         }
//     }
//     printf("Answer :- \n");
//     for(i=0;i<3;i++){
//         for(j=0;j<3;j++){
//             printf("  %d  ",c[i][j]);
//         }
//         printf("\n");
//     }
    
// }

// // 12.	Write a C program to find the roots of a quadratic equation.

// #include<stdio.h>
// #include<math.h>
// int main() {
//     int a,b,c,d;
//     printf("Formet of quadratic equaction is :- \n ax^2 + bx + c =0 \n enter a , b , c :-");
//     scanf("%d%d%d",&a,&b,&c);
//     printf("your quadratic equaction is :- %dx^2 + %dx + %d \n",a,b,c);
    
//     d=(pow(b,2)-(4*a*c));
//     printf("D = %d \n",d);
//     if (d<0){
//         printf("Roots is imegenery .\n");
//     }else if(d==0){
//         printf("Roots are same \n");
//     }else{
//         printf("Roots are real \n");
//     }
//     float root1= (-b+sqrt(d))/(2*a);
//     float root2= (-b-sqrt(d))/(2*a);
//     printf("Root 1 = %f \nRoot 2 = %f",root1,root2);
// }

// // 1.	Write a C program to find all the prime numbers between 100 to 500.
// #include<stdio.h>
// int main() {
//     int a,i,j;
//     for(i=100;i<500;i++){
//         a=0;
//         for(j=2;j<i;j++){
//             if(i%j==0){
//                 a=1;
//             }
//         }
//         if(a!=1){
//             printf("%d \n",i);
//         }
//     }
// }