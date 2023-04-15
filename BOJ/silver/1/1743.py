import sys
sys.stdin = open('./input.txt')

sys.setrecursionlimit(10000)
direction = [(1,0),(-1,0),(0,-1),(0,1)]

def boundary_check (y, x):
    if y < 0 or x < 0 or y >= n or x >= m:
        return False
    return True

cnt = 1
def dfs(y, x):
    global cnt
    visited[y][x] = True
    for dir in direction:
        next_y = y + dir[0]
        next_x = x + dir[1]
        if not boundary_check(next_y,next_x):
            continue
        if board[next_y][next_x] == 1 and not visited[next_y][next_x]:
            cnt += 1
            visited[next_y][next_x] = True
            dfs(next_y,next_x)
    return cnt

n,m,k = map(int,input().split())
board = [[0] * m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

answer = 1
for i in range(n):
    for j in range(m):
        if board[i][j]==1 and not visited[i][j]:
            answer = max(dfs(i,j), answer)
            cnt = 1

print(answer)
