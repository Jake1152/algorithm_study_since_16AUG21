#include "bits/stdc++.h"


using namespace std;


int pnt[1001]={0};

int get_pnt(int a) {
    return pnt[a]==0? a:get_pnt(pnt[a]);
}
bool up_pnt(int a, int b) {
    int p_a=get_pnt(a), p_b=get_pnt(b);
    if(p_a==p_b) return false;

    pnt[p_a]=p_b;

    return true;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int N,M,a,b,c,answer=0;
    vector<pair<int,pair<int,int>>> com;
    cin>>N>>M;
    for (int i = 0; i < M; i++) {
        cin>>a>>b>>c;
        com.push_back({c,{a,b}});
    }
    sort(com.begin(),com.end());
    for(int i=0;i<M;i++){
        a=com[i].second.first;
        b=com[i].second.second;
        c=com[i].first;
        if (up_pnt(a, b)) {
            answer += c;
        }
    }
    cout<<answer;
    return 0;
}
