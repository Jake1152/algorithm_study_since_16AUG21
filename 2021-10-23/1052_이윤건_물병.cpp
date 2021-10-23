#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int N,K;
    cin>>N>>K;
    for(int i=0;;i++){
        int num=N+i,cnt=0;
        while(num){
            if(num%2) cnt++;
            num/=2;
        }
        if(cnt<=K){
            cout<<i;
            return 0;
        }
    }
}
