////////////////////////bionery to decimal
// #include <iostream>
// using namespace std;
// // #include <math.h>
// int po(int a,int b){
//     int i,j=0,n=1;
//     for(i=1;i<=b;i++){
//         n=n*a;
//     }
//     // cout << n<<"end"<<endl;
//     return n;
// }
// int main () {
//     //bionery to decimal
//     cout << "enter bionery number :- ";
//     int n,i,j=0,num=0;
//     cin>>n;
//     while(n){
//         i=n%10;
//         if(i==1){
//             int s=po(2,j);
//             num=num+ s;
//         }
//         j++;
//         n=n/10;
//     }
//     cout<<num;
// }
///////////////// decimal to bionery
// #include <iostream>
// using namespace std;
// int main() {
//     int n,i,j=0,num[100];
//     cout <<"enter number :- ";
//     cin >> n;
//     while(n){
//         i=n%2;
//         num[j]=i;
//         n=n/2;
//         j++;
//     }
//     while((j-1)){
//         cout<<num[j];
//         j--;
//     }
//     // cout << num;
// }
//////////revarce a interer 
// #include <iostream>
// using namespace std;
// int main(){
//     cout<<"enter number : -";
//     int num,i,j,k=0;
//     cin >> num;
//     while(num){
//         i=num % 10;
//         k=k*10+i;
//         num = num / 10;
//     }
//     // cout <<k;
//     if (k >=9223372036854775807 || k <=-9223372036854775808){
//         printf("0");
//     }else{
//         printf("%d",k);
//     }
//     // cout << INTMAX_MIN;
    
// }
////////////// complement any bionery number(*****)
// #include <iostream>
// using namespace std;
// int main() {
//     int n=7,num=0;
//     cout << "enter number :- \n";
//     // cin>>n;
//     int m=n;
//     while(m!=0){
//         num=(num<<1)|1;
//         m=m>>1;
//     }
//     int ans= (~n)&num;

//     cout << "ans "<<ans;
// }
////////////it is power of 2 or not
#include <iostream>
using namespace std;
int main() {
    int n=4,i,j=1;
    for(i=0;i<n;i++){
        j=j*2;
        if(j<=n){
            if(j==n){
                cout << "it is power of 2";
            }else{continue;}
        }else{break;}
    }
} 