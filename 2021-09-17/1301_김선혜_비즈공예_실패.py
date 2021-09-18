
import sys
sys.setrecursionlimit((10**6))

def dfs(first, second, third, forth, fifth, prev, prev_prev):
    if first == 0 and second == 0 and third == 0 and forth == 0 and fifth == 0:
        return 1

    if first < 0 or second < 0 or third < 0 or forth < 0 or fifth < 0:
        return 0

    ret = 0

    if first >= 1 and prev != 1 and prev_prev != 1:
        ret += dfs(first - 1, second, third, forth, fifth, 1, prev)

    if second >= 1 and prev != 2 and prev_prev != 2:
        ret += dfs(first, second - 1, third, forth, fifth, 2, prev)

    if third >= 1 and prev != 3 and prev_prev != 3:
        ret += dfs(first, second, third - 1, forth, fifth, 3, prev)

    if forth >= 1 and prev != 4 and prev_prev != 4:
        ret += dfs(first, second, third, forth - 1, fifth, 4, prev)

    if fifth >= 1 and prev != 5 and prev_prev != 5:
        ret += dfs(first, second, third, forth, fifth - 1, 5, prev)

    return ret

if __name__ == '__main__':
    N = int(input())

    marble_list = [0, 0, 0, 0, 0]
    for i in range(N):
        marble_list[i] = int(input())

    result = dfs(marble_list[0], marble_list[1], marble_list[2], marble_list[3], marble_list[4], -1, -1)
    print(result)
