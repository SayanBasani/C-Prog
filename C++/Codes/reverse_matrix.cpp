#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int re(vector<vector<int>> &a){
    for(int i = 0 ; i < a.size() ; i++){
        for(int j = 0 ; j < i ; j++){
            swap(a[i][j] , a[j][i]);
        } 
    }
    
    for(int i = 0 ; i < a.size() ; i++){
        reverse(a[i].begin(),a[i].end());
    }
    for(int i = 0 ; i < a.size() ; i++){
        for(int j = 0 ; j < a.size() ; j++){
            cout << a[i][j] << " ";
        }
        cout<<endl;
    }
}
int main() {
    vector<vector<int>> a ={{1,2,3},{4,5,6},{7,8,9}};
    re(a);
   
}