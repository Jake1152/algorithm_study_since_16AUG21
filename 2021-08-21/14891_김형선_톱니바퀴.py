gears = []
for _ in range(4):
    gears.append([input(), 0])

def get_west(gear):
    return gear[0][(gear[1] - 2) % 8]

def get_east(gear):
    return gear[0][(gear[1] + 2) % 8]

def is_rotatable(gear_index1, gear_index2):
    return get_east(gears[min(gear_index1, gear_index2)]) != get_west(gears[max(gear_index1, gear_index2)])

def rotate(index, next_index, direction):
    if (index < 0 or index >= 4):
        return
    if (next_index >= 0 and next_index < 4 and is_rotatable(index, next_index)):
        rotate(next_index, next_index + (next_index - index), -direction)
    gears[index][1] = (gears[index][1] - direction) % 8

for _ in range(int(input())):
    index, direction = map(int, input().split())
    index -= 1
    if index != 0 and is_rotatable(index - 1, index):
        rotate(index, index + 1, direction)
        rotate(index - 1, index - 2, -direction)
    else:
        rotate(index, index + 1, direction)

result = 0
for i in range(4):
    result += pow(2, i) * int(gears[i][0][gears[i][1]])
print(result)




    

