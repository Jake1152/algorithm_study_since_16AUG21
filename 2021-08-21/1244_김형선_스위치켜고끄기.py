N = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    gender, num = map(int, input().split())
    if (gender == 1):
        for i in range(num, N + 1, num):
            switch[i - 1] = 1 - switch[i - 1]
    else:
        switch[num - 1] = 1 - switch[num - 1]
        i, j = num - 2, num
        while (i >= 0 and j < N and switch[i] == switch[j]):
            switch[i] = 1 - switch[i]
            switch[j] = 1 - switch[j]
            i -= 1
            j += 1
while (len(switch) > 20):
    print(' '.join(list(map(str, switch[:20]))))
    switch = switch[20:]
print(' '.join(list(map(str, switch[:20]))))
