#other person code1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def pre_order(in_start,in_end, post_start, post_end):
	# base case
	if (in_start > in_end) or (post_start > post_end):
		return
	
	# post order 끝이 root임을 이용
	parents = post_order[post_end]
	print(parents, end = " ")
	
	# in order에서 root를 기준으로 좌우로 갈라지는 것을 이용
	left = position[parents] - in_start
	right = in_end - position[parents]
	
	# left, right로 나누어서 분할 정복 방식으로 트리를 추적하여 pre-order를 찾는다.
	pre_order(in_start, in_start+left-1, post_start, post_start+left-1) # left sub-tree
	pre_order(in_end-right+1, in_end, post_end-right, post_end-1) #right sub-treee

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

#post-order 끝값이 in-order 어디 인덱스에 위치하는지 확인위해
#in-order 값들의 인덱스값을 저장
position = [0]*(n+1)
for i in range(n):
	position[in_order[i]] = i

# in-order, post-order 모두 0부터 n-1 값을 주고 pre-order를 구한다.
pre_order(0, n-1, 0, n-1)