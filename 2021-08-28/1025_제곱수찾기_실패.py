import math
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))

answer = -1
for y in range(N):
    for x in range(M):
        for dy in range(-y, N - y):
            for dx in range(-x, M - x):
                step_x, step_y = x, y
                num = 0
                while (0 <= step_x and step_x < M) and (0 <= step_y and step_y < N):
                    num *= 10
                    num += board[step_y][step_x]
                    if (dx == 0 and dy == 0):
                        break
                    step_y, step_x = step_y + dy, step_x + dx
                sqrt = math.sqrt(num)
                if (int(sqrt) == sqrt):
                    answer = max(answer, num)

print(answer)
