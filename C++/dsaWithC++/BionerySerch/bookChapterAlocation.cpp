// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;
bool check(vector<int> arr,int mid,int n,int m){
	int count_chapter=1,count_page=0;
        cout<<"chapter = "<<count_chapter<<"  .  ";
        cout<<" pages are = ";
	for(int i=0;i<m;i++){
		if(count_page+arr[i]<=mid){
            cout<<arr[i]<<" ";
			count_page += arr[i];
		}
        else{
        cout<<" total page is = "<<count_page<<endl;
            cout<<endl;
			count_chapter++;
			if(count_chapter>n || arr[i]>mid){
                cout<<"   false return"<<endl;
				return false;
			}
            cout<<"chapter = "<<count_chapter<<"  .  ";
			count_page=arr[i];
            cout<<" pages are = "<<arr[i] << " ";

		}
	}
    cout<<" total page is = "<<count_page<<endl;

    cout<<"   true return"<<endl;

	return true;
} 
long long ayushGivesNinjatest(int n, int m, vector<int> time) 
{	
	// Write your code here.
	int total_time=0;
	for(int i=0;i<m;i++){
		total_time += time[i];
	}
	int s=0,e=total_time,ans=-1;
	int mid=s+(e-s)/2;
	while(s<=e){
        cout<<"start = "<<s<<" end is = "<<e<<endl;
        cout<<"mid is = "<<mid<<endl;
		if(check(time,mid,n,m)){
            cout<<endl<<endl;
			ans=mid;
			e=mid-1;
		}else{
			s=mid+1;
		}
		mid=s+(e-s)/2;
	}
	return ans;
}
int main(){
    vector<int> arr={30,20,10,40,5,45};
    int n=3,m=6;
    int result=ayushGivesNinjatest(n,m,arr);
    cout<<"answer is "<<endl;
    cout<<result;
    cout<<"..."<<endl;
    
}