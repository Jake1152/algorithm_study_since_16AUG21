#1244 스위치 켜고 끄기

def switch_handler(gender, s_th):    
    # 남학생, 받은 수의 배수의 스위치상태 변경
    if gender == 1:
        for s_idx in range(s_th-1, s_cnt, s_th):
            switches[s_idx] = 1 if switches[s_idx]== 0 else 0
    else: # 여학생, 받은 위치로부터 좌우대칭
        s_idx = s_th-1
        switches[s_idx] = 1 if switches[s_idx]== 0 else 0
        prev_s, next_s = s_idx-1, s_idx+1
        while prev_s >= 0 and next_s < s_cnt \
            and switches[prev_s] == switches[next_s]:
            switches[prev_s] = 1 if switches[prev_s]== 0 else 0
            switches[next_s] = 1 if switches[next_s]== 0 else 0
            prev_s -= 1
            next_s += 1

s_cnt = int(input())
switches = list(map(int, input().split()))
times = int(input())
for th in range(times):
    gender, s_th = map(int, input().split())
    switch_handler(gender, s_th)
    # print(f"\n{th=}\n{switches=}")

for idx in range(len(switches)-1):
    print(switches[idx], end=' ')
print(switches[len(switches)-1], end='')