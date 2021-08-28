from collections import deque

dx = [0, 0, 1, 0, 0, -1]
dy = [0, 1, 0, 0, -1, 0]
dz = [1, 0, 0, -1, 0, 0]

def solve(L, R, C):
    building = []
    start, end = None, None
    for z in range(L):
        floor = []
        for y in range(R):
            line = input()
            if 'S' in line:
                start = (line.find('S'), y, z)
            elif 'E' in line:
                end = (line.find('E'), y, z)
            floor.append(line)
        _ = input()
        building.append(floor)

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    q = deque()
    q.append((start, 0))
    visited[start[2]][start[1]][start[0]] = True
    while q:
        cursor, minutes = q.popleft()
        for i in range(6):
            x, y, z = cursor[0] + dx[i], cursor[1] + dy[i], cursor[2] + dz[i]
            if ((x, y, z) == end):
                print(f"Escaped in {minutes + 1} minute(s).")
                return
            if ((0 <= x < C) and (0 <= y < R) and (0 <= z < L) and
                    not visited[z][y][x] and building[z][y][x] == '.'):
                q.append(((x,y,z), minutes + 1))
                visited[z][y][x] = True
    print("Trapped!")

while (True):
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    solve(L, R, C)
