import sys
sys.setrecursionlimit(10**6)

def solution(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return

    parentNode = postOrder[postorder_end]
    print(parentNode, end=" ")

    left = inorder_idx_dict[parentNode] - inorder_start
    right = inorder_end - inorder_idx_dict[parentNode]

    solution(inorder_start, inorder_start+left-1, postorder_start, postorder_start+left-1) # 왼쪽
    solution(inorder_end-right+1, inorder_end, postorder_end-right, postorder_end-1) # 오른쪽 서브트리


if __name__ == '__main__':
    n = int(input())

    global inOrder, postOrder, inorder_idx_dict
    inOrder = list(map(int, input().split()))
    postOrder = list(map(int, input().split()))

    inorder_idx_dict = dict()
    for idx, num in enumerate(inOrder):
        inorder_idx_dict[num] = idx

    solution(0, n-1, 0, n-1)
