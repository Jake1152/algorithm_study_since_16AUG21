from collections import deque

N = int(input())
contestants = [0] + list(map(int, input().split()))
q = deque(range(1, N + 1))
answer = [None] * N
time = 0
while (len(q) != 0):
    time += 1
    i = q.popleft()
    contestants[i] -= 1
    if (contestants[i] == 0):
        answer[i - 1] = str(time)
    else:
        q.append(i)
print(" ".join(answer))
