# 욕심쟁이 판다
# 시간 : 1시간

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 1

def boundary(i, j):
    return 0 <= i < n and 0 <= j < n

def dfs(i, j):
    global ans
    # 이미 방문했다면 해당 지점의 dp값부터 시작 -> 리턴
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 1 # 기본 방문 체크
    for k in d:
        ni = i + k[0]
        nj = j + k[1]
        if not boundary(ni, nj):
            continue
        if g[i][j] < g[ni][nj]:
            count = 1   
            count += dfs(ni, nj)
            dp[i][j] = max(dp[i][j], count) # dfs가 풀릴 때 풀리는 지점을 기준으로 거리 갱신
            ans = max(ans, dp[i][j]) # 가장 먼 거리 갱신
    return dp[i][j]

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dfs(i, j)
print(ans)