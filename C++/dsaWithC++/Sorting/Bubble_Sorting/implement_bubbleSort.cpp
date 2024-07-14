#include <iostream>
using namespace std;
int printarr(int arr[],int size){
    cout<<"Printing This array"<<endl;
    for(int i=0;i<size;i++){
        cout<<arr[i]<<endl;
    }
}
int bubbleSort(int arr[],int size){
    for(int i=0;i<size-1;i++){
        for(int j=1;j<size-i-1;j++){
            if(arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
            }
        }
    }
}
int main(){
    // BUBBLE SORTING 
    int arr[6]={6,3,8,4,5,1},size=6;
    bubbleSort(arr,size);
    printarr(arr,size);
    
}