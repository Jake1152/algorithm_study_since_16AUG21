import sys
sys.setrecursionlimit(10000)

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

visited = [([-1] * N) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def search(x, y):
    if (visited[y][x] != -1):
        return visited[y][x]
    visited[y][x] = 1
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if (0 > new_x or new_x >= N) or (0 > new_y or new_y >= N) or (forest[new_y][new_x] <= forest[y][x]):
            continue
        visited[y][x] = max(1 + search(new_x, new_y), visited[y][x])
    return visited[y][x]

answer = 0
for x in range(N):
    for y in range(N):
        answer = max(answer, search(x, y))
print(answer)
