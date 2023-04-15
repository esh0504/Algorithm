import sys
from collections import deque

sys.stdin = open('./input.txt')


from collections import deque
def bfs(i):
    visited = [False] * (n+1)
    visited[i] = True
    queue = deque()
    queue.append(i)
    cnt = 0
    answer = [103] * n
    while(queue):
        for _ in range(len(queue)):
            node = queue.popleft()
            answer[node] = cnt
            for attr in board[node]:
                if not visited[attr]:
                    queue.append(attr)
                    visited[node] = True
        cnt += 1
    return sum(answer)

n, m = map(int,input().split())
board = [[] for i in range(n)]

for i in range(n):
    a,b = map(int,input().split())
    board[a-1].append(b-1)
    board[b-1].append(a-1)

answer = []
for i in range(n):
    answer.append(bfs(i))
print(answer)
print(answer.index(min(answer)) + 1)