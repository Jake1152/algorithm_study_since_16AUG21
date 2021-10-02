N = int(input())
people = list(map(int, input().split()))
limit = int(input())

dp = [[0 for j in range(N + 1)] for i in range(4)]
S = [0 for j in range(N + 1)]

for i in range(1, N + 1):
    S[i] = S[i - 1] + people[i - 1]

for i in range(1, 4):
    for j in range(N + 1):
        dp[i][j] = max(dp[i][j - 1], (dp[i - 1][j - limit] + S[j] - S[j - limit]))
print(dp[3][N])
