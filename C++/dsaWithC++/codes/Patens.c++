/* Printing of patens -1
        *  *  *  *  * 
        *  *  *  *  * 
        *  *  *  *  * 
        *  *  *  *  * 
        *  *  *  *  *
    */
/*
#include <iostream>
using namespace std;
int main () {
    int i=0,n,j;
    cout << "enter number :- ";
    cin>>n;
    while (i<n)
    {
        i=i+1;
        j=0;
        while(j<n){
            j=j+1;
            cout << " * ";
        }
        cout << endl;
    }
    
}
*/
/* Printing of patens -2
        1  2  3  4
        1  2  3  4
        1  2  3  4
        1  2  3  4
*/
/*
#include <iostream>
using namespace std;
int main () {
    int i=1,n,j=1;
    cout << "enter number :- ";
    cin >> n;
    while (i<=n){
        i++;
        int k=1,j=1;
        while(j<=n){
            cout<<" "<<j++<<" ";
        }
        cout << endl;
    }
}
*/
/* Printing of patens -3
        1 2 3
        4 5 6
        7 8 9
*/
/*
#include <iostream>
using namespace std ;
int main () {
    int n,i=1,j=1,k=1,l;
    cout <<"enter number :- ";
    cin >> n;
    while(i++<=n){
        j=1;
        while(j++<=n){
            cout <<" " <<k++<<" ";
        }
        cout << endl;
    }
}
*/
/* Printing of patens -4
*
* *
* * *
*/

// #include <iostream>
// using namespace std;
// int main() {
//     int n,i=0,j;
//     cout <<"enter name :- ";
//     cin >>n;
//     while (i++<n){
//         j=0;
//         while(j++<i){
//             cout << " *";
//         }
//         cout << endl;
//     }
// }
/* Printing of patens 
1
2 2
3 3 3
*/
// #include <iostream>
// using namespace std;
// int main() {
//     int i=0,j=0,k,n;
//     cout << "enter number :- ";
//     cin >> n;
//     while (i++<n){
//         j=0;
//         while(j++<i){
//             cout<<" " <<i;
//         }
//         cout << endl;
//     }
// }
/* Printing of patens -5
1
2 3
4 5 6
*/
// #include <iostream>
// using namespace std;
// int main () {
//     int n,i=0,j,k=1;
//     cout<< "enter number :- ";
//     cin >> n;
//     while (i++<n){
//         j=0;
//         while(j++<i){
//             cout << " " <<k++;
//         }
//         cout << endl;
//     }
// }
/* Printing of patens -6
1
1 2
2 3 4
4 5 6 7
*/
// #include <iostream>
// using namespace std;
// int main () {
//     int n,i=0,j=0,k=2;
//     cout <<"enter number : -";
//     cin >> n;
//     while(i++<n){
//         k=k-1;
//         j=0;
//         while(j++<i){
//             cout << " " <<k++;
//         }cout << endl;
//     }
// }
/* Printing of patens -7
1
2 3
3 4 5
4 5 6 7
*/
// #include <iostream>
// using namespace std;
// int main () {
//     int n,i=0,j=0,k;
//     cout<<"enter number :- ";
//     cin >> n;
//     while(i++<n){
//         j=0;
//         k=i;
//         while(j++<i){
//             cout<< k++;
//         }
//         cout<< endl;
//     }
// }
/* Printing of patens -8
1
2 1
3 2 1
4 3 2 1 
*/
// Ans-1
// #include <iostream>
// using namespace std;
// int main () {
//     int n,i=0,j,k,l;
//     cout <<"enter number :- ";
//     cin >> n;
//     while(i++<n){
//         j=0;
//         k=i;
//         while(j++<i){
//             cout <<" "<< k-- ;
//         }
//         cout <<endl ;
//     }
// }
// Ans-2
// #include <iostream>
// using namespace std;
// int main () {
//     int n,i=0,j,k,l;
//     cout <<"enter number :- ";
//     cin >> n;
//     while(i++<n){
//         j=0;
//         k=i;
//         while(j++<i){
//             // cout <<" "<< k-- ;
//             cout <<" "<< i-j+1 ;
//         }
//         cout <<endl ;
//     }
// }
/* Printing of patens -9
AAA
BBB
CCC
*/
/*
#include <iostream>
using namespace std;
int main() {
    int n,i=0,j=0,k=65;
    cout<<char(65);
    cout <<"enter number :- ";
    cin >> n;
    while(i++<n){
        j=0;
        while(j++<n){
            cout<<char(k);
        }
        cout<<endl;
        k++;
    }
}
*/
/* Printing of patens -10
A B C
A B C
A B C
*/
/*
#include <iostream>
using namespace std;
int main() {
    int row =0, col =0, n;
    cout << "enter number :- ";
    cin >> n;
    while (row ++<n){
        col =0;
        while(col++<n){
            char ch='A'+col-3;
            cout << ch <<" ";
        }
        cout << endl;
    }
}*/
/* Printing of patens -11
      *  n-i
    * *
  * * *
* * * *
*/
// #include <iostream>
// using namespace std;
// int main () {
//     int row =0 , col =0 ,n,i=1,j,k,l;
//     cout << "enter name :- ";
//     cin >> n;
//     while(row++ <n){
//         l=n-row;
//         // cout << row<<"  ";
//         while(l-->=0){
//             cout << " ";
//         }
//         j=row;
//         while (j-->=1){
//             cout << "*";
//         }
        
//         cout << endl;
//     }
// }
/* Printing of patens - 12
* * * *
* * * 
* * 
* 

*/
// #include <iostream>
// using namespace std;
// int main() {
//     int row =0,col = 0,i,j,n;
//     cout << "enter number :- ";
//     cin >> n;
//     while(row++<n){
//         col=0;
//         while(col++<(n-row+1)){
//             cout << "* ";
//         }
//         cout << endl;
//     }
// }
/* Printing of patens -12
* * * *
  * * *
    * *
      *
*/
// #include <iostream>
// using namespace std;
// int main() {
//     int row =0,col=0,n,i,k,j=0;
//     cout << "enter number :- ";
//     cin >> n;
//     while (row++<n){
//         k=n-row;
//         col =0;
//         i=n-(n-row)-1;
//         while(i-->=0){
//             cout << " ";
//         }
//         while (k--){
//             cout << "*";
//         }
//         cout <<endl;
//     }
// }
/* Printing of patens :-13 
      1 
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
*/
// #include<iostream>
// using namespace std;
// int main() {
//     int row =1,col=1,i,j,k,n,l;
//     cout <<" enter numbr :- ";
//     cin >>n;
//     while(row<=n){
//         col=1;
//         i=n-row;
//         while(i){
//             cout <<" ";
//             i=i-1;
//         }
//         j=1;k=row;
//         while(k){
//             cout<<j++;
//             k--;
//         }
//         k=row-1;j=row-1;
//         while(k){
//             cout<<j--;
//             k--;
//         }
//         row=row+1;
//         cout<<endl;
//     }
// }
/* Printing of patens :- 14
1 2 3 4 5 5 4 3 2 1
1 2 3 4 * * 4 3 2 1
1 2 3 * * * * 3 2 1
1 2 * * * * * * 2 1
1 * * * * * * * * 1
*/
// #include <iostream>
// using namespace std;
// int main() {
//     int row =1, col=1,n;
//     cout<<"enter number :- ";
//     cin >> n;
//     int r=1;
//     while(r<=n){
//         //first traningle
//         int c1=n-(r-1),count1=1;
//         while(c1-->0){
//             cout<<count1;
//             count1++;
//         }
//         //second traningle
//         int c2=n-(n-r)-1;
//         while(c2>0){
//             cout<<"*";
//             c2=c2-1;
//         }
//         //thard traingal
//         int c3=n-(n-r)-1;
//         while(c3>0){
//             cout<<"*";
//             c3--;
//         }
//         //forth traingal
//         int c4=n-r+1;
//         int count2=n;
//         while(c4>0){
//             cout<<count2--;
//             c4--;
//         }
//         cout << endl;
//         r=r+1;
//     }
// }
/*
// sum of integers 
#include <iostream>
using namespace std;
int main() {
    int sum=0,i=0,n;
    cout << "enter number :- ";
    cin >> n;
    while(i<=n){
        sum = sum +i ;
        i++;
    }
    cout << "sum of 0 to "<< n << " is "<<sum;
}
*/
/*
// find prime number 
#include <iostream>
using namespace std;
int main() {
    int i=2,n,j=0;
    cout << "enter number :- ";
    cin >> n;
    while(i<n){
        if(n%i==0){
            j=1;
        }
        i++;
    }
    if(j==1){
        cout  << "it is not prime number";
    }else if(j==0){
        cout << "it is prime number";
    }
}
*/
/*
print:-     1 1 1 1 1 1
            2 2 2 2 2 2
            3 3 3 3 3 3
            4 4 4 4 4 4
            5 5 5 5 5 5
            6 6 6 6 6 6
*/
/*
#include <iostream>
using namespace std;
int main(){
    int n,i=1,j;
    cout << "enter number :- ";
    cin >> n;
    while(i<=n){
        j=0;
        while(j<n){
            cout<<i<<" ";
            j++;
        }
        cout<< endl;
        i++;
    }
}
*/
// febonatchi series
// #include<iostream>
// using namespace std;
// int main () {
//     int n,i,a=0,b=1,sam;
//     cout << "enter number : -";
//     cin >> n;
//     for (i=0;i<n;i++){
//         sam =a+b;
//         cout <<i<<" febonatchi number is :-"<< sam << endl ;
//         a=b;
//         b=sam;

//     }
// }
// treacky question
// #include <iostream>
// using namespace std;
// int main() {
//     for (int i=0;i<=5;i++){
//         cout << i<< endl;
//         cout << i<< endl;
//         i++;
//         cout << i<< endl;
//         cout << i<< endl;
//         cout <<"on the time of iteration "<<i<<endl;
//     }
// }