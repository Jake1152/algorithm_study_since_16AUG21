from sys import stdin
from collections import defaultdict
input = stdin.readline
N, K = map(int, input().split())
bottle_dict = defaultdict(int)
bottle_dict[1] = N
new_bottle = 0
while (N <= K):
    for key, value in bottle_dict.items():
        if value % 2 == 0:
            bottle_dict[key] -= 1
            bottle_dict[value*2] += 1
            break
    else:
        print(-1)
        break
    N -= 1

print(new_bottle)

'''
N,


---
5 3

101
011

1 1 1 1 1 
2 1 1 1
2 2 1 
3
0

3 1
11
01
1

'''