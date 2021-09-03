from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
graph = [ [] for _ in range(N+1)]

in_degree = [0 for _ in range(N+1)]
q = deque()
result = []

for _ in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)
	in_degree[e] += 1

for i in range(1, N+1):
	if in_degree[i] == 0:
		q.append(i)

while q:
	a = q.popleft()
	result.append(a)
	for t in graph[a]:
		in_degree[t] -= 1
		if in_degree[t] == 0:
			q.append(t)

print(*result)
# *쓰면 리스트를 unpacking한다.
# When calling a function, 
# the * operator can be used to unpack an iterable into the arguments in the function call