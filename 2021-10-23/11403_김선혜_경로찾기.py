import sys
sys.setrecursionlimit((10**9))

def dynamic(a, y, x):
    visit[a][x] = 1

    for i in range(N):
        if graph[x][i] == 1 and visit[a][i] == 0:
            dynamic(a, y, i)


if __name__ == "__main__":
    N = int(input())
    graph = list()
    for i in range(N):
        row = list(map(int, input().split()))
        graph.append(row)

    visit = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and visit[i][j] == 0:
                dynamic(i, i, j)

    for i in range(N):
        for j in range(N):
            print(visit[i][j], end=' ')
        print()
