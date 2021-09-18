import sys
from itertools import combinations

input = sys.stdin.readline
N,D,K = map(int,input().split())
arr=[]
answer=0
for i in range(N):
    arr.append(list(map(int,input().split()))[1:])
for per in combinations(range(1,D+1),K):
    cnt=0
    for a in arr:
        if set(a)-set(per) == set():
            cnt+=1
    answer=max(answer,cnt)
print(answer)

