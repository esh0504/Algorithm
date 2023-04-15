import sys
sys.stdin = open('./input.txt')

from collections import deque

def dfs(i, cnt):
    if visit[i] == 1:
        return arr[i]
    visit[i] = 1
    for index in range(len(board[i])):
        if visit[board[i][index]] == 1:
            return cnt + arr[board[i][index]]
        else:
            arr[board[i][index]] += 1
            return dfs(board[i][index], cnt + 1)
    return cnt

def bfs(i):
    q = deque([i])
    visited = [False] * n
    visited[i] = True
    cnt = 1
    while q:
        v = q.popleft()
        for node in board[v]:
            if not visited[node]:
                cnt += 1
                visited[node] = True
                q.append(node)
    return cnt
n, m = map(int, input().split())
board = [[] for i in range(n)]
visit = [0] * (n)

for i in range(m):
    a,b = map(int, input().split())
    board[b-1].append(a-1)

arr = [0] * n
for i in range(n):
    arr[i] = bfs(i)

for i in range(n):
    if max(arr) == arr[i]:
        print(i + 1, end=' ')
