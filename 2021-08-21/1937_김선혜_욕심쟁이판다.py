from sys import setrecursionlimit
setrecursionlimit(10**9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, visited, forestMap):
    if visited[x][y]:
        return visited[x][y]

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if forestMap[x][y] < forestMap[nx][ny]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny, visited, forestMap) + 1)

    return visited[x][y]


if __name__ == '__main__':
    global n
    n = int(input())
    forestMap = list()
    visited = list()

    for i in range(n):
        row = list(map(int, input().split()))
        forestMap.append(row)
    visited = [[0] * n for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, dfs(i, j, visited, forestMap))

    print(ans)
