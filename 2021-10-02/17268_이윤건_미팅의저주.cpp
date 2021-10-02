#include "bits/stdc++.h"


using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    int N;
    long long DP[5001]={1,1};
    cin>>N;
    N/=2; //N쌍의 커플이 만들어짐..

    for (int i = 2; i <= N; i++) {
        for (int j = 0; j < i; j++) {
            DP[i]+=DP[j]*DP[i-1-j];
            DP[i]%=987654321;
        }
    }
    cout<<DP[N];

    return 0;
}
