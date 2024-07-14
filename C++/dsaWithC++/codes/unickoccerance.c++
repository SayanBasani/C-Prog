#include <iostream>
using namespace std;
int print(int arr[],int size){
    for(int i=0;i<size;i++){
        cout<< " "<< arr[i] << " ";
    }
    cout << endl;
}
int swapp(int &a,int &b){
    int c= a;
    a=b;
    b=c;
}
int sor(int arr[] , int size){
    int ans[10],in=0;
    int p=arr[0];
    
    int left = 0 ,right = size-1;
    for(int i=0;i<size;i++){
        int n=arr[i];
        for(int j=i+1;j<size;j++){
            if(n>arr[j]){
                swapp(n,arr[j]);
            }
        }
    }
}
int main(){
    int arr[8]={0,1,5,8,9,};
    sor(arr,8);
    print(arr,8);
}