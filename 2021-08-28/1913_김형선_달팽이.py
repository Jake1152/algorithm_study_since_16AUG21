N = int(input())
target = int(input())
board = [[None] * N for _ in range(N)]

x, y = N // 2, N // 2
target_x, target_y = x, y
count = 1
board[y][x] = str(count)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
i = 0
for n in range(1, N + 2):
    for _ in range(2):
        for _ in range(1, n):
            count += 1
            x += dx[i]
            y += dy[i]
            if (target == count):
                target_x, target_y = (x, y)
            if (count > N * N):
                break
            board[y][x] = str(count)
        i = (i + 1) % 4

for i in range(len(board)):
    print(' '.join(board[i]))
print(target_y + 1, target_x + 1)
