import sys
sys.stdin = open('./input.txt')

from collections import deque

def init_board_():
    return [[0 for col in range(501)] for row in range(501)]

d_x = [1,0,-1,0]
d_y = [0,1,0,-1]

def boundary_check(y,x):
    if y < 0 or x < 0 or y> 500 or x >500:
        return False
    return True
def bfs(board):
    life = 0
    answer = []
    check_board = init_board_()
    q = deque()
    q.append((0,0,0))
    while(len(q)!=0):
        y,x,c = q.popleft()
        check_board[y][x] = 1
        if y==500 and x==500:
            return c
        if check_board[y][x] == 1:
            continue
        for i in range(4):
            next_y = y+d_y[i]
            next_x = x+d_x[i]
            if not boundary_check(next_y, next_x):
                continue
            if board[next_y][next_x]==1:
                q.append((next_y,next_x,c+1))
            elif board[next_y][next_x] == 2:
                continue
            else:
                q.appendleft((next_y,next_x,c))


    return -1

board = init_board_()
n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(min(y1,y2),max(y1,y2)+1):
        for col in range(min(x1,x2), max(x1,x2)+1):
            board[row][col] = 1
m = int(input())
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(min(y1,y2),max(y1,y2)+1):
        for col in range(min(x1,x2), max(x1,x2)+1):
            board[row][col] = 2
answer = bfs(board)

print(answer)


