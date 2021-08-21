import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
people = list()
for _ in range(k):
    k, v = map(int, input().split())
    people.append([k, v])

def boy(i):
    while i <= n:
        if i > n:
            return
        if arr[i - 1]:
            arr[i - 1] = 0
        else: 
            arr[i - 1] = 1
        i += i

def girl(i):
    if i == 1:
        if arr[i]:
            arr[i] = 0
        else:
            arr[i] = 1
        return
    if i == len(arr):
        if arr[i - 1]:
            arr[i - 1] = 0
        else:
            arr[i - 1] = 1
        return

    before, after = i - 1, i + 1
    while 0 < before and after <= len(arr):
        if arr[before - 1] == arr[after - 1]:
            before -= 1
            after += 1
            if before <= 0:
                for idx in range(before, after - 1):
                    if arr[idx]:
                        arr[idx] = 0
                    else:
                        arr[idx] = 1
                return
            continue
        else:
            if arr[i - 1]:
                arr[i - 1] = 0
            else:
                arr[i - 1] = 1
        
for k, v in people:
    if k == 1:
        boy(v)
    else:
        girl(v)
print(" ".join(map(str, arr)))