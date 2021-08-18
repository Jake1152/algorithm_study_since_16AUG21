#include "bits/stdc++.h"

using namespace std;


int s,N,K;
bool get_color(int r, int c,int t){
    if(t==0) return 0;
    int p_r=r/t, p_c=c/t;
    int b=(N-K)/2;
    if(b<=p_r && p_r<b+K && b<=p_c && p_c<b+K) return 1;
    return get_color(r%t,c%t,t/N);
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int R1,R2,C1,C2;
    cin>>s>>N>>K>>R1>>R2>>C1>>C2;
    
    int P=1;
    while(s--) P*=N;
    
    for(int r=R1;r<=R2;r++){
        for(int c=C1;c<=C2;c++){
            cout<<get_color(r,c,P);
        }
        cout<<'\n';
    }

    
    return 0;
}
