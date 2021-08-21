# 1713 후보 추천하기 
from collections import Counter
from collections import defaultdict

candi_cnt = int(input())
reco_cnt = int(input())
candi = defaultdict(int)
for reco in map(int, input().split()):
    least_cnt = reco_cnt+1
    if len(candi) >= candi_cnt:
        for c in candi:
            if least_cnt > c:
                least_cnt = c
        for c in candi:
            if c ==least_cnt:
                


    candi[reco] += 1

for ele in Counter(candi).most_common(reco_cnt):
    print(ele, end=' ')