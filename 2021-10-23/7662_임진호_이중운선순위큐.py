import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    minq, maxq = [], []
    visited = [False for _ in range(1000001)]
    for i in range(int(input())):
        alpha, num = input().split()
        if alpha == 'I':
            heapq.heappush(minq, (int(num), i))
            heapq.heappush(maxq, (-int(num), i))
            visited[i] = True
        elif num == '-1':
            while minq and not visited[minq[0][1]]:
                heapq.heappop(minq)
            if minq:
                visited[minq[0][1]] = False
                heapq.heappop(minq)
        else:
            while maxq and not visited[maxq[0][1]]:
                heapq.heappop(maxq)
            if maxq:
                visited[maxq[0][1]] = False
                heapq.heappop(maxq)
    
    while minq and not visited[minq[0][1]]: heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]: heapq.heappop(maxq)
    print(f'{-maxq[0][0]} {minq[0][0]}' if maxq and minq else'EMPTY')