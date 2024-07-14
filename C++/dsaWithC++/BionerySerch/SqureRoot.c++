#include <iostream>
using namespace std;
int sqrooint(int num){
    int s=0,e=num;
    int mid=(e+s)/2;
    while(s<=e){
        int x=mid*mid;
        if(x==num){
            return mid;
        }else if(x>num){
            e=mid-1;
        }else if(x<num){
            s=mid+1;
        }
        mid = (s+e)/2;
    }
}
int main(){
    int n=17;
    cout << sqrooint(n);

}