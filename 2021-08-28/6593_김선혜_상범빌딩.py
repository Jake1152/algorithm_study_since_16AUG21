from collections import deque
import sys
sys.setrecursionlimit(10**6)

# 동서남북상하
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    q = deque()
    q.append([sz, sy, sx])
    visit[sz][sy][sx] = 1

    while q:
        z, y, x = q.popleft()
        for i in range(6):
            now_x = x + dx[i]
            now_y = y + dy[i]
            now_z = z + dz[i]
            if 0 <= now_z < L and 0 <= now_y < R and 0 <= now_x < C:
                if building_map[now_z][now_y][now_x] == "E":
                    print("Escaped in {} minute(s).".format(visit[z][y][x]))
                    return
                elif building_map[now_z][now_y][now_x] == "." and visit[now_z][now_y][now_x] == 0:
                    visit[now_z][now_y][now_x] = visit[z][y][x] + 1
                    q.append([now_z, now_y, now_x])

    print("Trapped!")
    return

if __name__ == '__main__':
    while True:
        L, R, C = map(int, input().split())

        if L == 0 and R == 0 and C == 0:
            break

        visit = [[[0] * C for i in range(R)] for j in range(L)]

        building_map = [[] * R for i in range(L)]

        for i in range(L):
            for j in range(R):
                append_building_list = list(map(str, input()))
                building_map[i].append(append_building_list)
                if 'S' in append_building_list:
                    sx, sy, sz = append_building_list.index('S'), j, i
                if 'E' in append_building_list:
                    ex, ey, ez = append_building_list.index('E'), j, i

            input()

        bfs()

