from collections import deque
import sys

def bfs(num_1, num_2, prime_num):
    q = deque()
    q.append([num_1, 0])
    visit = [0 for _ in range(10000)]

    visit[num_1] = 1
    while q:
        num, cnt = q.popleft()
        if num == num_2:
            return cnt

        if num < 1000:
            continue
        for i in [1, 10, 100, 1000]:
            n = num - num % (i * 10) // i * i
            for j in range(10):
                if visit[n] == 0 and prime_num[n]:
                    visit[n] = 1
                    q.append([n, cnt + 1])
                n += i

if __name__ == '__main__':
    input = sys.stdin.readline
    prime_num = [True for i in range(10001)]
    for i in range(2, 101):
        if prime_num[i]:
            j = i * 2
            while j < 10001:
                prime_num[j] = False
                j += i

    test = int(input())
    for i in range(test):
        num_1, num_2 = map(int, input().split())
        result = bfs(num_1, num_2, prime_num)
        if result != None:
            print(result)
        else:
            print("Impossible")
