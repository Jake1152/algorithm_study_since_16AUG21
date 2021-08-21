
def switch_change_man(student_num, switch):
    for i in range(student_num, len(switch) + 1, student_num):
        switch = change(i - 1, switch)


def change(num, switch):
    if switch[num] == 0:
        switch[num] = 1
    elif switch[num] == 1:
        switch[num] = 0
    return switch


def switch_change_woman(student_num, switch):
    switch = change(student_num, switch)

    N = len(switch)
    for i in range(1, N//2):
        if (student_num + i) > (N-1) or (student_num - i) < 0:
            break

        if switch[student_num + i] == switch[student_num - i]:
            switch = change(student_num + i, switch)
            switch = change(student_num - i, switch)
        else:
            break


if __name__ == '__main__':
    switch_num = int(input())
    switch = list(map(int, input().split()))

    student = int(input())
    for i in range(student):
        gender, student_num = map(int, input().split())

        if gender == 1: # 남자
            switch_change_man(student_num, switch)
        elif gender == 2: # 여자
            switch_change_woman(student_num - 1, switch)

    for index, data in enumerate(switch):
        print(data, end=" ")
        if index % 19 == 0 and index != 0:
            print()

