# boj 2493 탑
# stack

# 탑의 개수
N = int(input())
# 탑 리스트
top_list = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
	while stack:
		# 수신 가능한 상황
		if stack[-1][1] > top_list[i]:
			answer.append(stack[-1][0] + 1)
			break
		else:
			stack.pop()
	#스택이 비게되면 수신할 탑이 없다.
	if not stack:
		answer.append(0)
	  # 인덱스, 값
	stack.append([i, top_list[i]])

print(" ".join(map(str, answer)))
