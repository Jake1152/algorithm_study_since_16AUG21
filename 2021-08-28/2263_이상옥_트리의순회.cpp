#include "bits/stdc++.h";
using namespace std;

pair<int, int> sub[100001];
int location[100001], N, post[100001];
int post_idx = 0;
vector<int> answer;
void dfs(int left) {
    if (post_idx == N - 1) return;
   
    int now = post[post_idx];
    int next = post[post_idx + 1];
    if (location[now] < location[next]) { //다음 노드의 인오더 위치가 오른쪽이면 오른쪽으로 갈 수 있음.
        post_idx++;
        dfs(location[next] - location[now] - 1);//go_right
        sub[now].second = next;
    }
    if (left == 0 || post_idx == N - 1) return; //왼쪽으로 갈 수 있는 경우가 없음.
    next = post[post_idx + 1];
    if (location[now] > location[next]) { //왼쪽 다 돌고 온 후 다음 인덱스가 왼쪽이면 왼쪽으로 갈 수 있음.
        post_idx++;
        dfs(left - (location[now] - location[next]));
        sub[now].first = next;
    }

}
void pre_order(int node) {
    if (!node) return;
    cout << node << ' ';
    pre_order(sub[node].first);
    pre_order(sub[node].second);
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int node;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> node;
        location[node] = i;
    }
    for (int i = N - 1; i >= 0; i--) {
        cin >> post[i];
    }

    dfs(location[post[0]]);

    pre_order(post[0]);

    return 0;
}


