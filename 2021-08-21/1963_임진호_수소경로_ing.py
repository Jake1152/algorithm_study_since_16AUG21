#1963 소수경로
from collections import deque

def sieve_of_Eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    
    prime_list = []
    for p in range(2, n+1):
        if prime[p]:
            prime_list.append(p)
    return prime_list

def make_adjacent_list(prime_list, num):
    a_set = set()
    for prime in prime_list:
        s_prime = str(prime)
        for n_idx, n_val in enumerate(str(num)):
            if n_val == s_prime[n_idx]:
                a_set.add(prime)                
    return list(a_set)

n = 10000
prime_list = sieve_of_Eratosthenes(n)

begin = 0
end = len(prime_list)
mid = 0
while begin <= end:
    mid = (begin + end)//2
    if prime_list[mid] >= 1000:
        begin = mid+1
    else:
        end = mid-1

# 1,000~10,000 사이의 소수
prime_list = prime_list[begin:]

times = int(input())
for _ in range(times):
    start, target = map(int, input().split())
    visited = [True for _ in range(len(prime_list))]
    q = deque()
    q = make_adjacent_list(prime_list, start)
    while (q):
        tmp = q.popleft()



'''
# 1
1. 1,000~10,000 사이의 소수 구하기
2. BFS
  시작숫자
  인접리스트 구성?

  목표숫자


# 2
1. 인접한 소수만 구한다.
    1개 자릿수라도 일치하는 소수
    target 소수와 일치여부도 중요
    target에 일치하는 수가 하나도 없다면?
    과정 최단경로가 될 수 있다고 보장할 수 있는가?
2. BFS

'''