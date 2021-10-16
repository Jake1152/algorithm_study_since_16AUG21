from sys import stdin

input = stdin.readline

def find_parent(x):
	if parent[x] != x:
		parent[x] = find_parent(parent[x])
	return parent[x]

def union_parent(a, b):
	a = find_parent(a)
	b = find_parent(b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]

edges = []
result = 0

for _ in range(m):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()

for edge in edges:
	cost, a, b = edge

	if find_parent(a) != find_parent(b):
		union_parent(a, b)
		result += cost

print(result)