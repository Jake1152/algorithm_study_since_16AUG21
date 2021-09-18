#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int DP[61][61][61];
    for(int i=0;i<61;i++){
        for(int j=0;j<61;j++){
            for(int k=0;k<61;k++){
                DP[i][j][k]=100000;
            }
        }
    }
    int mutal[6][3]={{1,3,9},{1,9,3},{3,1,9},{3,9,1},{9,1,3},{9,3,1}};
    DP[0][0][0]=0;
    
    for(int i=0;i<61;i++){
        for(int j=0;j<61;j++){
            for(int k=0;k<61;k++){
                for(int m=0;m<6;m++){
                    DP[i][j][k]=min(DP[i][j][k],
                                    DP[max(0,i-mutal[m][0])][max(0,j-mutal[m][1])][max(0,k-mutal[m][2])]+1);
                }
            }
        }
    }
    
    int arr[3]={0},N;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>arr[i];
    }
    cout<<DP[arr[0]][arr[1]][arr[2]];
    return 0;
}
