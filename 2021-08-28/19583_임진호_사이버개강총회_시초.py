from sys import stdin

input = stdin.readline
attendance = []
cnt = 0

S, E, Q = input().split(' ')

s_to_min = int(S[0:2]) * 60 + int(S[3:5])
e_to_min = int(E[0:2]) * 60 + int(E[3:5])
q_to_min = int(Q[0:2]) * 60 + int(Q[3:5])

while (True):
	try:
		time, id = input().split(' ')
		# 입장확인		
		time_to_min = int(time[0:2]) * 60 + int(time[3:5])		
		if 0 <= time_to_min <= s_to_min:
			attendance.append(id)
		# 퇴장확인
		elif  id in attendance and \
			e_to_min <= time_to_min <= q_to_min:
			cnt += 1
	except:
		break
print(cnt)