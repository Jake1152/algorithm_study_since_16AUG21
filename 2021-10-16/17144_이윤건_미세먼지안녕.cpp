#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int A[52][52],di[]={1,-1,0,0}, dj[]={0,0,1,-1};
    int R,C,T;
    int C_r, C_c;
    cin>>R>>C>>T;
    memset(A,-1,sizeof(A));
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            cin>>A[i][j];
            if(A[i][j]==-1){
                C_r=i;
                C_c=j;
            }
        }
    }
    while(T--){
        int ex_A[51][51]={0};
        for (int i = 1; i <= R; i++) {
            for (int j = 1; j <= C; j++) {
                int ex=A[i][j]/5;
                for (int d = 0; d < 4; d++) {
                    int ni=i+di[d], nj=j+dj[d];
                    if(A[ni][nj]==-1) continue;
                    A[i][j]-=ex;
                    ex_A[ni][nj]+=ex;
                }
                ex_A[i][j]+=A[i][j];
            }
        } //첫번째 확산

        //두번째 공기청정기
        //반시계방향 회전
        int i=C_r-1, j=C_c,pre=0;
        int half=i-1+C;
        for(int h=1;h<half;h++){
            if(j==C) i--;
            else j++;
            swap(pre,ex_A[i][j]);
        }
        for (int h = 1; h < half; h++) {
            if (j == 1) i++;
            else j--;
            swap(pre,ex_A[i][j]);
        }
        //시계방향 회전
        i = C_r, j = C_c, pre = 0;
        half = (R-i) + C;
        for (int h = 1; h < half; h++) {
            if (j == C) i++;
            else j++;
            swap(pre, ex_A[i][j]);
        }
        for (int h = 1; h < half; h++) {
            if (j == 1) i--;
            else j--;
            swap(pre, ex_A[i][j]);
        }
        for (int i = 1; i <= R; i++) {
            for (int j = 1; j <= C; j++) {
                A[i][j] = ex_A[i][j];
            }
        }
        //공기 청정기 다시 냅둠
        A[C_r-1][C_c]=-1; A[C_r][C_c]=-1;
    }
    int answer=2;
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            answer+=A[i][j];
        }
    }
    cout<<answer;
    
    return 0;
}
