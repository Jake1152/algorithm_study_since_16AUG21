#include "bits/stdc++.h"

using namespace std;


int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    int N, M,a,b;
    int in[32001]={0};
    vector<int> out[32001];
    cin>>N>>M;
    for (int i = 0; i < M; i++) {
        cin>>a>>b;
        out[a].push_back(b);
        in[b]++;
    }
    queue<int> Q;
    for (int i = 1; i <= N; i++) {
        if(in[i]==0) Q.push(i);
    }
    string answer="";
    int cnt=0;
    while (Q.size()) {
        int q=Q.front();Q.pop();
        answer+=to_string(q)+" ";
        for (int o : out[q]) {
            if(--in[o]==0) Q.push(o);
        }
    }
    cout<<answer;
    return 0;
}
