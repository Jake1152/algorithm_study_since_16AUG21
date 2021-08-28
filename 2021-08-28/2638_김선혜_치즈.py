import sys
sys.setrecursionlimit((10**6))
# 좌우상하
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def solution(x, y):
    for i in range(4):
        now_x = x + dx[i]
        now_y = y + dy[i]

        if 0 <= now_y < n and 0 <= now_x < m and not visit[now_y][now_x]:
            if cheese_list[now_y][now_x] != 0:
                cheese_list[now_y][now_x] += 1
            else:
                visit[now_y][now_x] = 1
                solution(now_x, now_y)


def melting_cheese():
    for i in range(n):
        for j in range(m):
            if cheese_list[i][j] != 0:
                return False

    return True


if __name__ == '__main__':
    global n, m
    n, m = map(int, input().split()) # n : 행 y, m: 열 x

    global cheese_list
    cheese_list = list()
    for _ in range(n):
        cheese_list.append(list(map(int, input().split())))

    hours = 0
    while True:
        if melting_cheese():
            print(hours)
            break

        global visit
        visit = [[0 for _ in range(m)] for _ in range(n)]
        solution(0, 0)

        for i in range(n):
            for j in range(m):
                if cheese_list[i][j] >= 3:
                    cheese_list[i][j] = 0
                elif cheese_list[i][j] > 0:
                    cheese_list[i][j] = 1
        hours += 1
