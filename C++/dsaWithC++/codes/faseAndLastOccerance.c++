//////////first and last position in a sorted array
#include<iostream>
using namespace std;
int firstOce(int arr[],int size,int key){
    int start = 0 , end=size-1,ans=-1;
    int mid = (start+end)/2;
    while(start<=end){
        if(arr[mid]==key){
            ans=mid;
            end=mid-1;
        }
        else if(key>arr[mid]){
            start=mid++;
        }
        else if(arr[mid]>key){
            end=mid-1;
        }
    int mid = (start+end)/2;
    }
    return ans;
}
int main(){
    int arr[5]={2,4,4,6,6},size=5,n=4;
    int a1=firstOce(arr,size,n);
    cout <<a1<<endl;
}