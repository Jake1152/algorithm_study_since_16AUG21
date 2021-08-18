#include "bits/stdc++.h";

using namespace std;

string gears[5];

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    priority_queue<pair<int,pair<int,int>>> locations;

    int DP[502][502]={0}, board[502][502]={0};
    int n,di[]={1,-1,0,0}, dj[]={0,0,1,-1};
    cin>>n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin>>board[i][j];
            locations.push({-board[i][j],{i,j}});
        }
    }

    int answer=0;
    while(locations.size()){
        auto location=locations.top();locations.pop();
        int i=location.second.first, j=location.second.second;
        answer=max(answer,DP[i][j]+1);
        for (int d = 0; d < 4; d++) {
            int ni=i+di[d], nj=j+dj[d];
            if(board[i][j] < board[ni][nj]) DP[ni][nj]=max(DP[ni][nj],DP[i][j]+1);
        }
    }
    cout<<answer;
    return 0;
}
