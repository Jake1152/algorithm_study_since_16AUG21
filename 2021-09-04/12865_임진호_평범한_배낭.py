from sys import stdin

input = stdin.readline
N, K = map(int, input().split())

item = [[0, 0]]
dp = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N):
	item.append(list(map(int, input().split())))


for i in range(1, N+1):
	for j in range(1, K+1):
		w = item[i][0]
		v = item[i][1]

		if j < w:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] =  max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])

# N, K = map(int, input().split())
# items = []
# v_result = 0
# for _ in range(N):
# 	 items.append(tuple(map(int, input().split())))

# print("items:", items)
# items_sorted = sorted(items, key = lambda x: x[1], reverse=True)

# for w, v in items_sorted:
# 	print("w:", w)
# 	print("v:", v)
# 	if K - w >= 0:
# 		v_result += v
# 		K -= w
# 	else:
# 		break
# print(v_result)