#include "bits/stdc++.h"

using namespace std;

int result=-1;

vector<int> getKMPJump(string str) {
    vector<int> answer = vector<int>(str.size(), -1);
    int i = 1, j = 0;
    for (; i < str.size(); i++) {
        if (str[0] == str[i]) break;
    }
    for (; i < str.size(); i++,j++) {
        if (str[i] == str[j]){
            result = max(result, j);
            answer[i] = j;
        }
        else {
            if (j == 0) j = -1;
            else{
                i--, j--;
                j = answer[j];
            }
        }
    }
    return answer;
}
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    string str;
    cin >> str;
    for (int s = 0; s < str.size(); s++) {
        getKMPJump(str.substr(s));
    }
    cout << result+1;
    return 0;
}
