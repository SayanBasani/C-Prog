#include <iostream>
#include <vector>
using namespace std;


int top(vector<int>& a){
    int top = a[0];
    for(int i = 0 ; i<a.size() ; i++){
        if(top < a[i]){
            top = a[i];
        }
    }
    return top;
}
int anss(vector<int>& a , int t){
    int ans = 0 ; 
    for(int i = 0 ; i < a.size();i++){
        ans +=(t - a[i]);
    }
    return ans;
}
int fin(vector<int>& a , int t){
    vector<int> add ;
    vector<int> co ;
    // int cou = 0;
    // int couu = 0 ;
    int ans = 0 ;
    int car_val=a[0];
    int top_af_t =0;
    for(int i = 1 ; i < a.size() ; i++){
        if(car_val > a[i] && car_val == t){
            co.push_back(a[i]);
            if(top_af_t < a[i]){
                top_af_t = a[i]; 
            }
        }
        else if(car_val > a[i] && car_val != t){
            co.push_back(a[i]);
        }else if(car_val < a[i]){
            ans += anss(co , car_val);
            co.clear();
        }
    }
    cout<<"end loop";
}
int main(){
    vector<int> a ={0,1,0,2};
    int t = top(a);
    cout<<"top value is :"<<t<<endl;
    fin(a,t);
}














// int fin(vector<int>& a , int t){
//     std :: vector<int> dev ;
//     for(int i = 0 ; i<a.size() ; i++){
//         // cout<<t-a[i];
//         dev.push_back(t-a[i]);
//         cout<<dev[i]<<endl;
//     }
//     for(int i = 0 ; i < dev.size() ; i++){
        
//     }
//     cout<<"end loop";
// }