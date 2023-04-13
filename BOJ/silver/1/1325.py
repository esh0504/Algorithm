import sys
sys.stdin = open('./input.txt')

from collections import deque
def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for i in board[node]:
            if check[i] == 0:
                check[i] = 1
                queue.append(i)

n, m = map(int, input().split())

board = [[] for _ in range(n+1)]

for i in range(m):
    src, dest = map(int,input().split())
    board[dest].append(src)

res = []

for i in range(1,n+1):
    check = [0] *(n+1)
    bfs(i)
    res.append(check.count(1))

m = max(res)

for i in range(n):
    if res[i] == m:
        print(i+1, end = ' ')

print()




