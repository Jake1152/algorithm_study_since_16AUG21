import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().strip()

n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

position = {}
for i in range(n):
	position[in_order[i]] = i

def recur(in_start, in_end, post_start, post_end):
	if (in_start > in_end) or (post_start > post_end):
		return
	root = post_order[post_end]
	print(root, end = ' ')
	p = position[root]
	left = p - in_start
	recur(in_start, p-1, post_start, post_start+left-1)
	recur(p+1, in_end, post_start+left, post_end-1)

recur(0, n-1, 0, n-1)