from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
rectangle = []
result = [ [ 0 for _ in range(m)] for _ in range(n)]
visisted = [ [ False for _ in range(m)] for _ in range(n)]
d = ((0,1), (0,-1), (1,0), (-1,0))

for _ in range(n):
	rectangle.append(list(input().rstrip()))

def bfs(x, y):
	q = deque()
	q.append(x, y)
	cnt =1
	ones = []

	while q:
		nx, ny = q.popleft()
		
		for i in range(4):
			nx = x + d[i][0]
			ny = y + d[i][1]
			
			if -1 < nx < n and -1 < ny < m:
				if visisted[nx][ny]:
					continue
				visisted[nx][ny] = True
				if rectangle[nx][ny] == 0:
					visisted[nx][ny] = True
					q.append((nx, ny))
					cnt += 1
				else:
					ones.append((nx,ny))
	for x, y in ones:
		visisted[x][y] = False
		result[x][y] += cnt
		if result[x][y] >= 10:
			result[x][y] %= 10
for i in range(n):
	for j in range(m):		
		if rectangle[i][j] == 0:
			if not visisted[i][j]:
				visisted[i][j] = True
				bfs(i, j)

for i in range(n):
	print(''.join(map(str, result[i])))

'''
bfs 매번
하지만 리셋
위치 바꿔가면서 진행
(0,0) ~ (n-1, n-1)

'''

