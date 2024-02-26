///////sum element in a array
// #include <iostream>
// using namespace std;
// int main (){
//     int arr[100],size,sum=0;
//     cout << "enter size of array :- ";
//     cin >> size;
//     for(int i=0;i<size;i++){
//         cin >>arr[i];
//         sum += arr[i];
//     }
//     cout << "sum of all number " <<sum <<endl;
// }
//////////revarce a array
// #include <iostream>
// using namespace std;
// int swp2(int *a,int *b){
//     int i=*a;
//     *a=*b;
//     *b=i;
// }
// int swip(int arr[],int size){
//     int j=size-1;
//     if(size%2==0){
//         size=size/2;
//         // cout<<size<<" it is even";
//     }else if(size%2==1){
//         size=(size/2)+1;
//     }
//     int sw;
//     for(int i=0;i<size;i++){
//         // sw=arr[i];
//         // arr[i]=arr[j];
//         // arr[j]=sw;
//         swp2(&arr[i],&arr[j]);
//         j--;
//     }
// }
// int main(){
//     int arr[100],size;
//     cout <<"enter size of array : -";
//     cin >> size ;
//     cout << "enter element :- ";
//     for(int i=0;i<size;i++){
//         cin >> arr[i];
//     }
//     swip(arr,size);
//     cout<<"after swap";
//     for(int i=0;i<size;i++){
//         cout << arr[i];
//     }
   
// }
////swap aulternet element if element are :- 1,2,3,4 so answer is :- 2,1,4,3
// #include <iostream>
// using namespace std;
// int main() {
//     int arr[100],size,size2;
//     cout<<"enter size of array :- "<<endl;
//     cin>>size;
//     for(int i=0;i<size;i++){
//         cin>>arr[i];
//     }
//     if(size%2!=0){
//         size2=size-1;
//     }else{
//         size2=size;
//     }
//     for(int i=0;i<size2;i+=2){
//         int k=arr[i];
//         arr[i]=arr[i+1];
//         arr[i+1]=k;
//     }
//     cout<<"after revarce :- "<<endl;
//     for(int i=0;i<size;i++){
//         cout<<arr[i]<<endl;
//     }
// }
//////print unique elements on array
// #include <iostream>
// using   namespace std;
// int inputarr(){
// }
// int main(){
//     int arr[100],size,arr2[100],coo=0;
//     cout << "enter size of array:- "<<endl;
//     cin >> size;
//     cout<<"enter elements :- "<<endl;
//     for(int i =0 ;i<size;i++){
//         cin>> arr[i];
//     }
//     for(int i=0;i<size;i++){
//         int c=1;
//         for(int j=0;j<size;j++){
//             if(i!=j){
//                 if(arr[i]==arr[j]){
//                     c=0;
//                     break;
//                 }
//             }
//         }
//         if(c==1){
//             cout<<"answer in to loop "<<arr[i]<<endl;
//             arr2[coo]=arr[i];coo++;
//         }
//     }
//     cout<<"answer :- "<<endl;
//     for(int z=0;z<coo;z++){
//         cout<<arr2[z]<<endl;
//     }
// }
////////find duplecat element
// #include <iostream>
// using namespace std;
// int dup(int arr[],int size){
//             cout<<"duplecat deleted :- "<<endl;
//     for(int i=0;i<size;i++){
//         for(int j=0;j<i;j++){
//             if(arr[i]==arr[j]){
//                 cout<<arr[i]<<endl;
//             }
//         }
//     }
// }
// int main() {
//     int arr[100],size,arr2[100],count=0;
//     cout<<"enter size of array :- ";
//     //input size
//     cin >> size ;
//     //input elements of array
//     for(int i=0;i<size;i++){
//         cin>>arr[i];
//     }
//     //final loop
//     for(int i=0;i<size;i++){
//         // cout<<"i = "<< i <<endl;
//         // int c=0;
//         for(int j=0;j<size;j++){
//             // cout<<"j = "<<j<<endl;
//             if(i!=j){
//                 // cout<<i<<"!="<<j<<endl;
//                 if(arr[i]==arr[j]){
//                     // c=1;
//                     arr2[count]=arr[i];
//                     count++;
//                     // cout<<"duplecat element are "<<arr[i]<<"count is "<<count<<endl;


//                 }   }
//         }
//             // if(c==1){
//             //     arr2[count]=arr[i];
//             //     cout<<"first element is "<<arr2[count]<<"count is "<<count<<endl;
//             //     count++;
//             // }
//     }

//     // cout<<"total duplecat found "<<count<<"answer :- ";
//     // for(int i=0;i<count;i++){
//     //     cout<<arr2[i]<<endl;
//     // }
//     dup(arr2,count);
//     cout<<"end";
// }
/////////////////////////////////////have to check 
////////find intersection on two array
// #include <iostream>
// using namespace std;
// int main(){
//     int arr1[10]={1,2,3,4,5,1,7,2,9,0},size1=10;
//     int arr2[10]={1,2,1,2,3},size2=5;
//     int arr[10],count=0;
//     for(int i=0;i<size1;i++){
//         for(int j=0;j<size2;j++){
//             if(arr1[i]==arr2[j]){
//                 arr[count]=arr2[j];
//                 count++;
//                 break;
//             }
//         }
//     }
//     for(int i=0;i<count;i++){
//         cout<<arr[i]<<endl;
//     }
// }
////////// arr short a array by 2 pointer aproch

// #include <iostream>
// using namespace std;
// int print(int arr[],int size){
//     for(int i=0;i<size;i++){
//         cout<< " "<< arr[i] << " ";
//     }
//     cout << endl;
// }
// int swapp(int &a,int &b){
//     int c= a;
//     a=b;
//     b=c;
// }
// int sor(int arr[] , int size){
//     int ans[10],in=0;
//     int p=arr[0];
    
//     int left = 0 ,right = size-1;
//     for(int i=0;i<size;i++){
//         int n=arr[i];
//         for(int j=i+1;j<size;j++){
//             if(n>arr[j]){
//                 swapp(n,arr[j]);
//             }
//         }
//     }
// }
// int main(){
//     int arr[8]={0,1,0,2,1,3,4,5};
//     sor(arr,8);
//     print(arr,8);
// }

//////////Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.



// class Solution {
// public:
//     bool uniqueOccurrences(vector<int>& arr) {
//         int size = arr.size();
//         int total[size],tot=0;
//         // all unick element
//         for(int i=0;i<size;i++){
//             int c=0;
//             for(int j=i+1;j<size;j++){
//                 if ( arr[i] == arr[j]){
//                     c=1;
//                     break;
//                 }
//             }
//             if(c==0){
//                 total[tot++]=arr[i];
//             }
//         }
//         // count from main which element how mach time present
//         int coun[tot],a=0;
//         for(int i=0;i<tot;i++){
//             int co=0;
//             for(int j=0;j<size;j++){
//                 if(total[i]==arr[j]){
//                     co++;
//                 }
//             }
//             coun[a++]=co;
//         }
//         int ans=0;
//         for(int i=0;i<a;i++){
//             for(int j=i+1;j<a;j++){
//                 if(coun[i]==coun[j]){
//                     ans=1;
//                     return false;
//                 }
//             }
//         }
//         return true;
//     }
// };

/// ////// find duplecates in an array return in a array

//##// its complexity is O(n^2)
// class Solution {
// public:
//     vector<int> findDuplicates(vector<int>& nums) {
//         int size=nums.size();
//         std :: vector<int> ans;
//         for(int i=0;i<size;i++){
//             for(int j=i+1;j<size;j++){
//                 if(nums[i]==nums[j]){
//                     ans.push_back(nums[i]);
//                 }
//             }
//         }
//         return ans;
//     }
// };