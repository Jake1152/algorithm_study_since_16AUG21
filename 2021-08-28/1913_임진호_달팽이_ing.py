'''
반시계방향으로 돌면서 채운다.
하, 우, 상, 좌
0이 아니면 방문한것으로 친다.
'''

n = int(input())
k = int(input())

square = [[ 0 for _ in range(n)] for _ in range(n)]
num = n*n
r = 0
c = 0
direc

while num:	
	square[r][c] = num
	num -= 1
	# 아래 오른 위 왼 이전에 가던 방향이 안될때만 이렇게 되어야한다.
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	for x, y in zip(dx, dy):		
		next_r = r + x
		next_c = c + y
		if 0 =< next_r < n and \
			0 =< next_c < n and:
			square[next_r][next_c] == 0:

	
