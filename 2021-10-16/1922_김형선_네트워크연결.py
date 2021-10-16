from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
que = PriorityQueue()

for _ in range(M):
    node1, node2, score = map(int, input().split())
    edges.append((score, {node1, node2}))

def find_and_put_edges_to_queue(node):
    for i in range(len(edges)-1, -1, -1):
        edge = edges[i]
        if node in edge[1]:
            que.put(edge)
            edges.pop(i)

answer = 0
node = list(edges[0][1])[0]
current_node_set = {node}
find_and_put_edges_to_queue(node)
while len(current_node_set) < N:
    edge = que.get_nowait()
    if len((edge[1] - current_node_set)) == 0:
        continue
    answer += edge[0]
    node = (edge[1] - current_node_set).pop()
    find_and_put_edges_to_queue(node)
    current_node_set.add(node)
print(answer)
