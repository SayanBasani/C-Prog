#include <iostream>
#include <vector>
using namespace std;

int top_index(vector<int>& nums, int target){
        int size=nums.size();
        int s=0,e=size-1;
        int big_i;
        while(s<e){
            int mid=s+(e-s)/2;
            if(s==mid){
                break;
            }else if(nums[s]>nums[mid]){
                big_i=s;
                e=mid;
            }else if(nums[mid]>nums[s]){
                big_i=mid;
                s=mid;
            }
        }
        return big_i;
    }
    bool search(vector<int>& nums, int target) {
        int size=nums.size();
        int s=0,e=size-1;
        int top_size;
        if(nums[0]>nums[e]){
            top_size=top_index(nums, target);
        }
        if(nums[e]>target){
            s=top_size+1;
        }else if(target>nums[e]){
            e=top_size;
        }
        int i=1;
        while(s<=e){
            cout<<"index "<<s<<" < "<<e<<endl;
            int mid=s+(e-s)/2;
            cout<< "middle is "<< mid<<endl;
            cout<<"compeared element "<<nums[mid] <<" and "<<target<<endl;
            if(nums[mid]==target){
                return true;
            }else if(nums[mid]>target){
                e=mid-1;
                cout<<"end dicrement "<<e << endl;
            }else if(target>nums[mid]){
                s=mid+1;
                cout<<"start increment "<<s<<endl;
            }
            cout<<"iteration "<<i++<<endl <<endl;
        }
        return false;
    }
int main ( ) {
    vector<int> arr={5,6,7,8,9,1,2,3,4};
    int ans = top_index(arr,3);
    bool tool = search(arr,9);
    cout<< "big index is "<< ans << endl;
    // cout<< "true is "<< true << endl;
    cout << "this "<<tool<<endl;
}