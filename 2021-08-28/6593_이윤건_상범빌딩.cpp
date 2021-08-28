#include "bits/stdc++.h";

using namespace std;

int dl[] = { 1,-1,0,0,0,0 }, dr[] = { 0,0,1,-1,0,0 }, dc[] = { 0,0,0,0,1,-1 };
char board[32][32][32];

string Escape(int L, int R, int C) {
    queue<pair<pair<int,int>,pair<int, int>>> Q;
    for (int l = 1; l <= L; l++) {
        for (int r = 1; r <= R; r++) {
            for (int c = 1; c <= C; c++) {
                cin >> board[l][r][c];
                if(board[l][r][c]=='S'){
                    Q.push({{0,l},{r,c}});
                }
            }
        }
    }
    while (Q.size()) {
        auto q = Q.front(); Q.pop();
        int cnt=q.first.first, l=q.first.second, r=q.second.first, c=q.second.second;
        for (int d = 0; d < 6; d++) {
            int nl=l+dl[d], nr=r+dr[d], nc=c+dc[d];
            if(board[nl][nr][nc]=='.'){
                board[nl][nr][nc] = 'S';
                Q.push({{cnt+1, nl},{nr,nc}});
            }
            if (board[nl][nr][nc] == 'E') return "Escaped in " + to_string(cnt+1) + " minute(s).\n";
        }

    }
    return "Trapped!\n";
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    int L,R,C;
    memset(board, '#', sizeof(board));

    while(1){
        cin >> L >> R >> C;
        if(L==0 && R==0 && C==0) return 0;
        cout<<Escape(L,R,C);
    }

    return 0;
}


