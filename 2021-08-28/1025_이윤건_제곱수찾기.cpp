#include "bits/stdc++.h";
#define check(i,j) (0<=i && i<N && 0<=j && j<M)

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    set<string> sq;
    int answer=-1;
    char arr[9][9];
    for (int i = 0; i < 40000; i++) {
        sq.insert(to_string(i*i));
    }
    int N,M;
    cin>>N>>M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin>>arr[i][j];
            if (arr[i][j]=='0' || arr[i][j]=='1' || arr[i][j]=='4' || arr[i][j]=='9')
                answer=max(answer,arr[i][j]-'0');
        }
    }

    for (int di = -N+1; di < N; di++) {
        for (int dj = -M+1; dj < M; dj++) {
            if(di==0&&dj==0) continue;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    string temp = "";
                    temp+=arr[i][j];
                    int ni=i+di, nj=j+dj;
                    while (check(ni, nj)) {
                        temp+=arr[ni][nj];
                        ni+=di; nj+=dj;
                        if(sq.find(temp)!=sq.end()) answer=max(answer,stoi(temp));
                    }
                }
            }
        }
    }
    cout<<answer;

    return 0;
}


