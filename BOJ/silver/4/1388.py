import sys
sys.stdin = open('./input.txt')

testCase = int(input())

def dfs(i,j):
    if visited[i][j]:
        return 0
    wall = board[i][j]
    visited[i][j] = True
    if wall == '|':
        if i >= n-1:
            return 1
        if board[i+1][j] == wall:
            return dfs(i+1, j)
        else:
            return 1
    else:

        if j >= m-1:
            return 1
        if board[i][j+1] == wall:
            return dfs(i, j+1)
        else:
            return 1


for _ in range(testCase):
n,m = map(int, input().split())
board = []
visited = [[False] * m for i in range(n)]
for i in range(n):
    board.append(input())
sum = 0
for i in range(n):
    for j in range(m):
        sum += dfs(i,j)
print(sum)