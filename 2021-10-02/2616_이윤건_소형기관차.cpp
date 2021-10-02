#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int N,K,arr[50000]={0},max_cus[4][50000]={0};
    cin>>N;

    for (int i = 0; i < N; i++) {
        cin>>arr[i];
    }
    cin>>K;
    int sum=0;
    queue<int> Q;
    for (int i = 0; i < N; i++) {
        Q.push(arr[i]);
        sum+=Q.back();
        if(Q.size()>K){
            sum-=Q.front();
            Q.pop();
        }
        max_cus[0][i]=sum;
        max_cus[1][i]=sum;
    }
    
    for (int i = 1; i < N; i++) {
        max_cus[1][i]= max(max_cus[1][i],max_cus[1][i-1]);
    }
    
    for (int train = 2; train < 4; train++) {
        for (int i = K; i < N; i++) {
            max_cus[train][i]=max(max_cus[train][i-1],max_cus[train-1][i-K]+max_cus[0][i]);
        }
    }
    cout<<max_cus[3][N-1];
    return 0;
}
