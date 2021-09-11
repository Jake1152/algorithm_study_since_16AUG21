#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int k,g[13],sum=0;
    cin>>k;
    for(int i=0;i<k;i++){
        cin>>g[i];
        sum+=g[i];
    }
    set<int> nums;
    nums.insert(0);
    for(int i=0;i<k;i++){
        set<int> new_nums;
        for(int num:nums){
            new_nums.insert(num+g[i]);
            new_nums.insert(abs(num-g[i]));
        }
        nums.insert(new_nums.begin(),new_nums.end());
    }
    cout<<sum-nums.size() + 1;
    
    return 0;
}
