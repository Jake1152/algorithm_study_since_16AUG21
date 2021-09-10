#include <stdio.h>
#include <vector>
#include <algorithm>

#define max(a,b) (a>b?a:b)
#define W things[i].first
#define V things[i].second

using namespace std;

vector<pair<int,int>> things;
vector<vector<int>> dp;
int N,K,a,b;

short DFS(int i,int K){
    if(i==N) return 0;
    if(dp[i][K]==-1) dp[i][K]=max(K-W<0?0:V+DFS(i+1,K-W), DFS(i+1,K));
    return dp[i][K];
}
int main(){
    scanf("%d%d",&N,&K);
    things.resize(N);
    dp.resize(N,vector<int>(K+1,-1));
    for(int i=0;i<N;i++)scanf("%d%d",&W,&V);
    sort(things.begin(),things.end());
    printf("%d",DFS(0,K));
    return 0;
}
