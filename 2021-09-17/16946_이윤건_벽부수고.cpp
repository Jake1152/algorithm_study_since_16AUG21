#include "bits/stdc++.h"

#define check(i,j) (0<=i && i<N && 0<=j && j<M)

using namespace std;

bool board[1000][1000]={0};
int N, M;
int di[]={1,-1,0,0}, dj[]={0,0,1,-1};
bool visited[1000][1000]={0};
int pnt[1000000],cnt[1000000];


int get_pnt(int a) {
    return (pnt[a]==-1?a:pnt[a] = get_pnt(pnt[a]));
}

void up_pnt(int a, int b) {
    int pa=get_pnt(a), pb=get_pnt(b);
    if(pa==pb) return;
    pnt[pa]=pb;
    cnt[pb]+=cnt[pa];
}

void dfs(int i,int j) {
    int answer=1;
    for (int d = 0; d < 4; d++) {
        int ni = i+di[d], nj=j+dj[d];
        if(!check(ni, nj)) continue; //바운더리 체크
        if(board[ni][nj] || visited[ni][nj]) continue; //벽이거나 방문했으면,
        up_pnt(i*M+j, ni*M+nj);
        visited[ni][nj] = 1;
        dfs(ni,nj);
    }
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    char c;
    cin>>N>>M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin>>c;
            board[i][j]=c=='1';
            pnt[i*M + j]=-1;
            cnt[i*M + j]=1;//각 집합은 1개가 있다.
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if(!board[i][j]){
                visited[i][j]=1;
                dfs(i,j);
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for(int j=0;j<M;j++){
            if (board[i][j]) {
                set<int> s;
                for (int d = 0; d < 4; d++) {
                    int ni=i+di[d], nj=j+dj[d];
                    if(check(ni,nj) && !board[ni][nj]) s.insert(get_pnt(ni*M+nj));
                }
                int answer=1;
                for(int k:s){
                    answer+=cnt[k];
                }
                cout<<answer%10;
            }
            else cout<<0;
        }
        cout<<'\n';
    }

    return 0;
}
