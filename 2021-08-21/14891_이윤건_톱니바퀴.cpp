#include "bits/stdc++.h";

using namespace std;

string gears[5];

void left_gear(int i, int dir) {
    if(i>1 && gears[i][6] != gears[i-1][2]) left_gear(i-1,-dir);
    rotate(gears[i].begin(), gears[i].begin() + (8-dir)%8,gears[i].end());
}

void right_gear(int i, int dir) {
    if (i<4 && gears[i][2] != gears[i+1][6]) right_gear(i+1, -dir);
    rotate(gears[i].begin(), gears[i].begin() + (8-dir)%8, gears[i].end());
}
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    for (int i = 1; i < 5; i++) {
        cin>>gears[i];
    }
    int K,i;
    int d;
    cin>>K;
    while (K--) {
        cin>>i>>d;
        string gear=gears[i];
        right_gear(i,d);
        gears[i]=gear;
        left_gear(i,d);
    }
    int answer=0;
    for(int i=0;i<4;i++){
        answer+=gears[i+1][0]-'0'<<i;
    }
    cout<<answer;
    return 0;
}
