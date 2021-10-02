#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    long long answer=0;
    int N;
    stack<pair<int,int>> st;
    cin>>N;
    while (N--) {
        int num;
        cin>>num;
        while (st.size() && st.top().first < num) {
            answer+=st.top().second;
            st.pop();
        }
        if(st.size() && st.top().first==num) st.top().second++;
        else st.push({num,1});
        answer+=st.top().second;
        if(st.size()==1) answer--;
    }
    cout<<answer;
    return 0;
}
