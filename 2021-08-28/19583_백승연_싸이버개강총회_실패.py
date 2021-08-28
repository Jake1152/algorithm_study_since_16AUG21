import sys

sys.stdin = open("19583.txt", "rt")

# input = sys.stdin.readline


if __name__ == "__main__":
    S, E, Q = map(str, input().split())

    start_S, end_S = S.split(":")
    start_S = int(start_S)
    end_S = int(end_S)

    start_E, end_E = E.split(":")
    start_E = int(start_E)
    end_E = int(end_E)

    start_Q, end_Q = Q.split(":")
    start_Q = int(start_Q)
    end_Q = int(end_Q)

    hash_m = dict()

    while True:
        try:
            time, name = input().split()
        except EOFError:
            break

        h_time, m_time = time.split(":")
        h_time = int(h_time)
        m_time = int(m_time)

        # 개강총회 입장 여부 확인
        if h_time < start_S:
            hash_m[name] = hash_m.get(name, 0) + 1
        elif h_time == start_S and m_time <= end_S:
            hash_m[name] = hash_m.get(name, 0) + 1

        # 개강총회 퇴장 여부 확인
        if start_E <= h_time < start_Q:
            if hash_m.get(name, 0) != 1:
                continue
            else:
                hash_m[name] = 2
        elif h_time == start_Q and m_time <= end_Q:
            if hash_m.get(name, 0) != 1:
                continue
            else:
                hash_m[name] = 2

        # 스트리밍 끝나면 끝
        elif h_time >= start_Q and m_time > end_Q:
            break


    cnt = 0
    for key in hash_m.keys():
        if hash_m[key] == 2:
            cnt += 1

    print(cnt)

