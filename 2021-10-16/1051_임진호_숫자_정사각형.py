def check_vertex(start_index, square_size):
	prev_vertex = rectangle[start_index[0]][start_index[1]]
	for dx, dy in (square_size, 0), (0, square_size), (square_size, square_size):
		x = start_index[0] + dx
		y = start_index[1] + dy
		if (x < n and y < m) and (prev_vertex != rectangle[x][y]):
			continue
		else:
			if x< n and y < m:
				start_index[1] += 1
			elif x >= n:
				start_index[1] += start_index[0] + 1
				start_index[0] += 1
			else:
				print(square_size ** 2)
				break
	else:
		return tuple(start_index)

	return (-1,-1)

n,  m = map(int, input().split())
rectangle = []
for _ in range(n):
	rectangle.append(list(map(int, list(input()))))
# print(f"{rectangle=}")

square_max_size = min(n,m)
start_index = [0, 0]
for square_size in range(square_max_size, 1, -1):	
	result_tuple = check_vertex(start_index, square_size)
	if result_tuple == (-1, -1): # 
		print(1)
		break
	elif result_tuple == tuple(start_index):
		print(square_size ** 2)
		break
	else:
		check_vertex(start_index, square_size)




'''
정사각형의 크기 

#문제이해
- 꼭지점이 모두 같은 가장 큰 정사각형의 너비를 반환 


# 문제해결방법 
- 가장 클수 있는 정사각형부터 
	꼭지점을 확인한다.
	같으면 return 
	아니라면 
	옆칸으로 이동한다.
	 행우선으로 진행
	 - 꼭지점 확인
	 - 다음으로 이동하는 루틴 
	 2가지 필요 
	 
	 


'''