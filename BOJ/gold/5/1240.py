import sys
from collections import deque
sys.stdin = open('input.txt')

n, m = map(int, input().split())

def sol(start_node, destination):
    q = deque()
    q.append((start_node, 0))
    visited = [False for _ in range(n+1)]
    visited[start_node] = True
    while q:
        start, dest = q.popleft()
        if start == destination:
            return dest
        for i, l in graph[start]:
            if not visited[i]:
                visited[i]=True
                q.append((i, dest+l))

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    n1, n2, l = map(int,input().split())
    graph[n1].append((n2,l))
    graph[n2].append((n1,l))


for _ in range(m):
    n1, n2 = map(int,input().split())
    print(sol(n1,n2))
