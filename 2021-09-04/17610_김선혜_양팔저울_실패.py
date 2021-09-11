
def solution(weight_list):
    result_list = list()
    for weight in weight_list:
        temp = [weight]
        for e in result_list:
            temp.append(weight + e)
            temp.append(abs(weight - e))

        result_list += temp

    result_list = list(set(result_list))

    return result_list


if __name__ == '__main__':
    wight_num = input()
    weight_list = list(map(int, input().split()))
    weight_list.sort()

    weight_sum = sum(weight_list)
    return_list = solution(weight_list)

    print(weight_sum - len(return_list))
