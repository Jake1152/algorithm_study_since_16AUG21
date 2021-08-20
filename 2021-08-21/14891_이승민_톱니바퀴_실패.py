# 톱니바퀴
# 시간 : 2시간
# 0: 12시, 2: 3시, 6: 9시
# N극은 0, S극은 1
# 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
# 0 회전 x

import sys
input = sys.stdin.readline
g1 = list(map(int, input().strip()))
g2 = list(map(int, input().strip()))
g3 = list(map(int, input().strip()))
g4 = list(map(int, input().strip()))

k = int(input())
case = [list(map(int, input().split())) for _ in range(k)]
ans = 0

def leftRotate(g):
    tmp = g[0]
    for i in range(7, -1, -1):
        tmp, g[i] = g[i], tmp

def rightRotate(g):
    tmp = g[-1]
    for i in range(8):
        tmp, g[i] = g[i], tmp

for wheelNum, d in case:
    rotateCheck = [0] * 5
    rotateCheck[wheelNum] = d

    while True:
        # 1
        if wheelNum == 1:
            if g1[2] == g2[6]:
                break
            else:
                if d == 1:
                    d = -1
                    rotateCheck[2] = -1
                else:
                    d = 1
                    rotateCheck[2] = 1
            if g2[2] == g3[6]:
                break
            else:
                if d == 1:
                    d = -1
                    rotateCheck[3] = -1 
                else:
                    d = 1
                    rotateCheck[3] = 1
            if g3[2] == g4[6]:
                break
            else:
                if d == 1:
                    rotateCheck[4] = -1
                else:
                    rotateCheck[4] = 1
            break

        # 2
        if wheelNum == 2:
            if g1[2] == g2[6]:
                pass
            else:
                if d == 1:
                    rotateCheck[1] = -1
                else:
                    rotateCheck[1] = 1
            if g2[2] == g3[6]:
                break
            else:
                if d == 1:
                    d = -1
                    rotateCheck[3] = -1
                else:
                    d = 1
                    rotateCheck[3] = 1
            if g3[2] == g4[6]:
                break
            else:
                if d == 1:
                    rotateCheck[4] = -1
                else:
                    rotateCheck[4] = 1
            break

        # 3
        if wheelNum == 3:
            if g3[2] == g4[6]:
                pass
            else:
                if d == 1:
                    rotateCheck[4] = -1
                else:
                    rotateCheck[4] = 1
            if g3[6] == g2[2]:
                break
            else:
                if d == 1:
                    d = -1
                    rotateCheck[2] = -1
                else:
                    d = 1
                    rotateCheck[2] = 1
            if g1[2] == g2[6]:
                break
            else:
                if d == 1:
                    rotateCheck[1] = -1
                else:
                    rotateCheck[1] = 1
            break

        # 4
        if wheelNum == 4:
            if g3[2] == g4[6]:
                break
            else:
                if d == 1:
                    d = -1
                    rotateCheck[3] = -1
                else:
                    d = 1
                    rotateCheck[3] = 1
            if g2[2] == g3[6]:
                break
            else:
                if d == 1:
                    d = -1
                    rotateCheck[2] = -1
                else:
                    d = 1
                    rotateCheck[2] = 1
            if g1[2] == g3[6]:
                break
            else:
                if d == 1:
                    rotateCheck[1] = -1
                else:
                    rotateCheck[1] = 1
            break

    for i in range(1, 5):
        if i == 1:
            if rotateCheck[i] == 1:
                rightRotate(g1)
                continue
            if rotateCheck[i] == -1:
                leftRotate(g1)
                continue
            continue
        if i == 2:
            if rotateCheck[i] == 1:
                rightRotate(g2)
                continue
            if rotateCheck[i] == -1:
                leftRotate(g2)
                continue
            continue
        if i == 3:
            if rotateCheck[i] == 1:
                rightRotate(g3)
                continue
            if rotateCheck[i] == -1:
                leftRotate(g3)
                continue
            continue
        if i == 4:
            if rotateCheck[i] == 1:
                rightRotate(g4)
                continue
            if rotateCheck[i] == -1:
                leftRotate(g4)
                continue
            continue

if g1[0] == 1:
    ans += 1
if g2[0] == 1:
    ans += 2
if g3[0] == 1:
    ans += 4
if g4[0] == 1:
    ans += 8
print(ans)