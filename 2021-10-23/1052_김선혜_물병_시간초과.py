
def sumWater(N):
    sum_cnt = 0
    while N > 0:
        if N % 2 == 1:
            sum_cnt += 1
        N = N // 2

    return sum_cnt

def Solution(N, K):
    bottle = 0
    while True:
        if sumWater(N) <= K:
            break
        bottle += 1
        N += 1

    return bottle

if __name__ == '__main__':
    N, K = map(int, input().split())

    answer = -1
    if N <= K:
        answer = 0
    else:
        answer = Solution(N, K)

    print(answer)

