#include <iostream>
using namespace std;
int insertion(int arr[] , int b){
    for(int i=1;i<b;i++){
        int j=i-1,k=arr[i];
        for(;j>=0;j--){
            if(arr[j]>k){
                arr[j+1]=arr[j];
            }
            else{
                break;
            }
        }
        arr[j+1]=k;
    }
}
int main(){
    int arr[6]={10,1,7,4,8};
    insertion(arr,6);
    for(int i=0;i<5;i++){
        cout<<arr[i]<<endl;
    }
}