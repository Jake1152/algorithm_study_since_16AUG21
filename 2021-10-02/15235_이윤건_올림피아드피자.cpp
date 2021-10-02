#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int N,pizza,time=0;
    queue<pair<int,int>> Q;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>pizza;
        Q.push({pizza,i});
    }
    int answer[1000];
    while(Q.size()){
        auto q=Q.front();Q.pop();
        time++;
        if(--q.first) Q.push({q.first,q.second});
        else answer[q.second]=time;
    }
    for(int i=0;i<N;i++){
        cout<<answer[i]<<' ';
    }
    return 0;
}
