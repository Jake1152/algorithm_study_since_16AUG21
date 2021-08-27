from collections import deque

results = []

def find_s(layer, row, col):
	for l in range(layer):
		for r in range(row):
			for c in range(col):
				if building[l][r][c] == 'S':
					return (l, r, c)	
	return (-1, -1, -1)

while (True):
	L, R, C = map(int, input().split())
	if L == 0 and R == 0 and C == 0:
		break
	visisted = [ [ [ True for _ in range(C)] for _ in range(R) ] for _ in range(L)]
	dis = [[[0]*C for _ in range(R)] for _ in range(L)]
	distance = 0
	visist_flag = True	
	building = []
	for _ in range(L):
		layer = []
		for _ in range(R):
			layer.append(list(str(input())))
		input() # for newline
		building.append(layer)	
	# 시작위치 좌표
	s_l, s_r, s_c = find_s(L, R, C)
	if s_l == -1:
		results.append(0)
		continue
	q = deque([(s_l, s_r, s_c)])	
	while q:		
		# 동북서남 상 하
		dx = [0, -1, 0, 1, 0, 0]
		dy = [1, 0, -1, 0, 0, 0]
		dz = [0, 0, 0, 0, 1, -1]			
		tmp = q.popleft()
		c_l, c_r, c_c = tmp
		#방문표시
		visisted[c_l][c_r][c_c] = False
		if building[c_l][c_r][c_c] == 'E':
			results.append(distance)
			visist_flag = False
			continue

		for x, y, z in zip(dx, dy, dz):
			l = c_l + x
			r = c_r + y
			c = c_c + z
			#빌딩내부이면서 방문도 안했고 갈수 있는 곳인 경우
			if 0 <= l < L and \
				0 <= r < R and \
				0 <= c < C and \
				visisted[l][r][c] and \
				building[l][r][c] != '#':
				q.append((l, r, c))
				dis[l][r][c] = dis[c_l][c_r][c_c] + 1				
				if dis[l][r][c] > distance:
					distance = dis[l][r][c]

	if visist_flag:
		results.append(0)

for result in results:
	if result != 0:
		print("Escaped in " + str(result) + " minute(s).")
	else:
		print("Trapped!")