# https://www.acmicpc.net/problem/1937

import sys
from collections import deque

sys.stdin = open("1937.txt", "rt")


# input = sys.stdin.readline


def BFS(x, y):
    global n
    global g
    queue = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    chk = [[False] * n for _ in range(n)]
    chk[x][y] = True
    queue.append((x, y))
    cnt = 1
    while queue:
        root_x, root_y = queue.popleft()
        for i in range(4):
            next_x = root_x + dx[i]
            next_y = root_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and not chk[next_x][next_y]:
                if g[root_x][root_y] < g[next_x][next_y]:
                    # 방문한 지점은 True로 초기화
                    chk[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    cnt += 1
    return cnt


if __name__ == "__main__":
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    # 1개 방문이 최소 카운트
    max_cnt = 1

    for x in range(n):
        for y in range(n):
            max_cnt = max(BFS(x, y), max_cnt)

    print(max_cnt)
