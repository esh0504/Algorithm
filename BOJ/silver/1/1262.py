import sys

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()

sys.stdin = open('./input.txt')

n, r1, c1, r2, c2 = map(int, input().split())
y = r1
x = c1

for i in range(r2-r1+1):
    x = c1
    for j in range(c2-c1+1):
        d_x = abs((n) - x % (2*n-1) - 1)
        d_y = abs((n) - y % (2*n-1) - 1)
        dist = d_x + d_y
        if dist >= n:
            print('.', end='')
        else:
            print(chr(dist%26 + 97),end='')
        x += 1
    y += 1
    print()

# for i in range(r1, r2):
#     for j in range(c1, c2):
#

# print_board(board)
# for i in range(r1, r2+r1+1):
#     for j in range(c1, c2+c1+1):
#         print(board[i%len(board)][j%len(board)], end=' ')
#     print()