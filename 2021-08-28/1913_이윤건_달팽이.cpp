#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    
    int N,arr[999][999],K;
    int x,y;
    cin>>N>>K;
    
    int i,j,L=1,d=0,di[]={-1,0,1,0},dj[]={0,1,0,-1}, cnt=1;

    i=j=N/2;
    while(true){
        for(int l=0;l<L;l++){
            if(cnt==K) x=i,y=j;
            arr[i][j]=cnt++;
            if(cnt>N*N) goto end;
            i+=di[d],j+=dj[d];
        }
        d=(d+1)%4;
        for(int l=0;l<L;l++){
            if(cnt==K) x=i,y=j;
            arr[i][j]=cnt++;
            if(cnt>N*N) goto end;
            i+=di[d],j+=dj[d];
        }
        d=(d+1)%4;L++;
    }
    end:
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout<<arr[i][j]<<' ';
        }cout<<'\n';
    }
    cout<<x+1<<' '<<y+1;
    return 0;
}
