import time

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(now_x, now_y):
    direction = 0
    now_num = N*N

    while True:
        if now_num <= 0:
            break


        if 0 <= now_y < N and 0 <= now_x < N and snail_list[now_y][now_x] == 0:
            snail_list[now_y][now_x] = now_num
            now_num -= 1
            now_x += dx[direction]
            now_y += dy[direction]

        else:
            now_x -= dx[direction]
            now_y -= dy[direction]
            direction = (direction + 1) % 4
            now_x += dx[direction]
            now_y += dy[direction]




if __name__ == '__main__':
    N = int(input())
    find_num = int(input())

    snail_list = [[0] * N for i in range(N)]

    solution(0, 0)


    for i in range(N):
        for j in range(N):
            print(snail_list[i][j], end=' ')
            if snail_list[i][j] == find_num:
                find_x, find_y = j + 1, i + 1
        print()

    print(find_y, find_x)
