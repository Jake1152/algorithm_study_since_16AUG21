# 14891 톱니바퀴
g = 4

def rotate(direc, turn, gears, g_idx):
	#clockwise
	g_len = len(gears[g_idx])
	if direc == 1:	
		gears[g_idx] = gears[g_idx][g_len-turn:]+gears[g_idx][:g_len-turn]
	elif direc == -1: #counterclockwise
		gears[g_idx] = gears[g_idx][turn:]+gears[g_idx][:turn]
	else:
		raise ValueError("unknown direction number :", direc)

def next_gear(gears, g_idx, direc):
	if (g_idx < 0) or (g_idx >= g):
		return
	visited[g_idx] = False
	#left bound
	if g_idx-1 > -1 and visited[g_idx-1] and \
		gears[g_idx][6] != gears[g_idx-1][2]:
		next_gear(gears, g_idx-1, direc*(-1)) 
	#right bound
	if g_idx+1 < g and visited[g_idx+1] and \
		gears[g_idx][2] != gears[g_idx+1][6]:
		next_gear(gears, g_idx+1, direc*(-1))
	
	rotate(direc, 1, gears, g_idx)
	# print("gears in: next_gear", gears, "\n")
	
	
def check_northbound(gears):
	result = 0
	for expo, gear in enumerate(gears):		
		cur = 2 ** expo if gear[0] == 1 else 0
		result += cur

	return result

gears = []
for _ in range(g):
	gears.append(list(map(int, list(input()))))
# print("gears:", gears, "\n")

times = int(input())
for _ in range(times):
	visited = [True for _ in range(g)]
	g_idx, direc = map(int, input().split())
	g_idx -= 1
	# print("g_idx, direc", g_idx, direc)
	next_gear(gears, g_idx, direc)

# print()
print(check_northbound(gears))

