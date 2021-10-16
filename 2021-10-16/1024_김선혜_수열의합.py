N, L = map(int, input().split())

bool_res = False
for i in range(L, 101):
    tempData = N - (i * (i-1) // 2)

    if tempData % i == 0 and tempData // i >= 0:
        res = tempData // i
        bool_res = True

        for j in range(i):
            print(res + j, end=(' '))

        break

if not bool_res:
    print(-1)
