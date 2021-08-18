#include "bits/stdc++.h";

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T;
    cin>>T;

    while(T--){
        bool none_prime[10000]={1,1};
        for (int i = 2; i < 1000; i++) {
            if(none_prime[i]) continue;
            none_prime[i] = 1;
            for (int j = i * i; j < 10000; j += i) {
                none_prime[j]=1;
            }
        }

        int prime,end;
        queue<pair<int,int>> Q;
        cin >> prime>>end;
        Q.push({0,prime});
        none_prime[prime]=1;
        while (Q.size()) {
            int cnt = Q.front().first,now = Q.front().second;
            if (now == end) {
                cout<<cnt<<'\n';
                break;
            }
            Q.pop();
            for(int k=1;k<10000;k*=10){
                for (int i = 0; i < 10*k; i+=k) {
                    int next= i + now - (now%(k*10)) + (now%k);
                    if (!none_prime[next]) {
                        Q.push({cnt+1,next});
                        none_prime[next] = 1;
                    }
                }
            }
        }
        if(Q.empty()) cout<<"Impossible\n";
    }
    return 0;
}
