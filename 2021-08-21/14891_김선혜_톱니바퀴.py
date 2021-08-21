
def checkLeft(gearNum, dir, gearList):
    if gearNum <= 0 or gearList[gearNum][6] == gearList[gearNum - 1][2]:
        return

    checkLeft(gearNum - 1, -dir, gearList)
    gearList[gearNum-1] = rotate(gearList[gearNum-1], dir)


def checkRight(gearNum, dir, gearList):
    if gearNum >= 3 or gearList[gearNum][2] == gearList[gearNum + 1][6]:
        return

    checkRight(gearNum + 1, -dir, gearList)
    gearList[gearNum+1] = rotate(gearList[gearNum+1], dir)


def rotate(r_list, dir):
    return r_list[-dir:] + r_list[:-dir]


if __name__ == "__main__":
    gearList = list()
    for i in range(4):
        row = list(map(str, input().split()))
        gearList.append(list(row[0]))

    n = int(input())
    for i in range(n):
        gearNum, dir = map(int, input().split())
        checkLeft(gearNum - 1, -dir, gearList)
        checkRight(gearNum - 1, -dir, gearList)
        gearList[gearNum - 1] = rotate(gearList[gearNum - 1], dir)

    result = 0
    for i in range(4):
        result += (2**i) * int(gearList[i][0])
    print(result)
