N, L = map(int, input().split())

answer = -1
for i in range(L, 101):
    if i % 2 == 0:
        temp = N / i + 0.5
        if temp == int(temp) and int(temp) - i//2 >= 0:
            answer = ' '.join(map(str, range(int(temp) - i//2, int(temp) + i//2)))
            break
    elif N % i == 0:
        answer = ' '.join(map(str, range(N//i - i//2, N//i + i//2 + 1)))
        break
print(answer)
