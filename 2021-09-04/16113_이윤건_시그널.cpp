#include "bits/stdc++.h"

using namespace std;

int col;
bool visited[5][20000]={0};
char sig[5][20000];

int dfs(int i, int j){
    if(0>i || i>=5 || 0>j || j>=col) return 0;
    if(visited[i][j]) return 0;
    visited[i][j]=1;
    if(sig[i][j]=='.') return 0;
    return 1+dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1);
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int n;
    
    cin>>n;
    
    col=n/5;
    for(int i=0;i<5;i++){
        for(int j=0;j<col;j++){
            cin>>sig[i][j];
        }
    }
    
    for(int j=0;j<col;j++){
        if(visited[0][j]) continue;
        switch (dfs(0,j)) {
            case 5:
                cout<<1;
                break;
            case 7:
                cout<<7;
                break;
            case 9:
                cout<<4;
                break;
            case 11:
                if(sig[3][j]=='#') cout<<2;
                else if(sig[1][j]=='.') cout<<3;
                else cout<<5;
                break;
            case 12:
                if(sig[2][j+1]=='.') cout<<0;
                else if(sig[1][j+2]=='.') cout<<6;
                else cout<<9;
                break;
            case 13:
                cout<<8;
                break;
        }
    }
    
    return 0;
}
