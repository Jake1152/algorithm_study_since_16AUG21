# 13335 트럭
from collections import deque
_, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
time = 0
total_weight = 0
on_the_bridge = deque()

truck = trucks.popleft()
total_weight += truck
# 트럭무게, 진입시간을 tuple로 on_the_bridge 큐에 넣는다.
on_the_bridge.append((truck, time))

while on_the_bridge:
	# print(f"{on_the_bridge=}")
	front_truck = on_the_bridge[0]
	entry_time = front_truck[1]
	# 다리에 맨앞에 트럭이 있는 경우, 다리가 하중을 견디면
	if w > time - entry_time and \
		trucks and \
		l >= total_weight + trucks[0]:
		truck = trucks.popleft()
		total_weight += truck
		on_the_bridge.append((truck, time+1))
	
	elif w <= time - entry_time : # 트럭이 다리를 지남, 새로운 트럭을 받아야한다.
		out_truck = on_the_bridge.popleft()
		total_weight -= out_truck[0]
		if trucks:
			truck = trucks.popleft()
			total_weight += truck
			on_the_bridge.append((truck, time+1))
			continue
	time += 1

print(time)

'''
다리에 있는 트럭들
현재 위치
현재 무게 총합
'''