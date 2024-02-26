#include <iostream>
#include <vector>
using namespace std;


int Selection(vector<int>& arr ){
    int size=arr.size();
    for(int i=0;i<arr.size();i++){
        int s;
        for(int j=i+1;j<size;j++){
            if(arr[i]>arr[j]){
                s=arr[i];
                arr[i]=arr[j];
                arr[j]=s;
            }
        }
    }
}

int main(){
    cout<<"It's ok"<<endl;
    vector <int> arr={5,4,3,2,1};
    Selection(arr);
    for(int i=0;i<arr.size();i++){
        cout<<arr[i]<<endl;
    }
}