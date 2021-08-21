from collections import deque
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False;
    return True;

def solve(first, last):
    if (first == last):
        print(0)
        return
    q = deque()
    q.append((first, 0))
    visited = {first}
    while (q):
        password, answer = q.popleft()
        for i in range(4):
            for j in range(10):
                if (i == 0 and j == 0):
                    continue
                new_password = password[:i] + str(j) + password[i + 1:]
                if (new_password == last):
                    print(answer + 1)
                    return
                if (new_password not in visited and is_prime(int(new_password))):
                    q.append((new_password, answer + 1))
                    visited.add(new_password)
    print("impossible")

for _ in range(int(input())):
    first, last = input().split()
    solve(first, last)
