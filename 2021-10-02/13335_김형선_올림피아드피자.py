n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0] * w 
answer = 0
while trucks or sum(bridge) > 0:
    answer += 1
    for i in range(w - 1, 0, -1):
        if i == w - 1:
            bridge[i] = 0
        bridge[i] = bridge[i - 1]
    bridge[0] = 0
    if (trucks and (sum(bridge) + trucks[0] <= L)):
        bridge[0] = (trucks.pop(0))
print(answer)
