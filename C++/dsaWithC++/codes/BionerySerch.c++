///////bionery search code
// #include <iostream>
// using namespace std;
// int pr(int arr[]){
//     int size=10;
//     for(int i=0;i<size;i++){
//         cout<<" "<<arr[i]<<" ";
//     }
//     cout<<endl;
// }
// int bio(int arr[],int find){
//     int size=10,j=0;
//     int mid=(0+size)/2;
//     for(int i=0;i<size;i++){
//         cout<<j++<<endl;
//         if(arr[mid]==find){
//             return mid;
//         }
//         else if(arr[mid]>find){
//             size=mid;
//         }
//         else if(arr[mid]<find){
//             i=mid;
//         }
//         mid=(i+size)/2;
//     }
//     return -1;
// }
// int main(){
//     //Binory Search
//     int arr[10]={1,2,3,4,5,6,7,90,99,100};
//     int fin=99;
//     pr(arr);
//     int a =bio(arr,fin) ;
//     cout << "ansewr "<<a<<" "<<arr[a]<< endl;
// }
