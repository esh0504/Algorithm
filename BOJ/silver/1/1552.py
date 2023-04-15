import sys
sys.stdin = open('./input.txt')


n = int(input())
board = [[0] * n for i in range(n)]
check_board = [[0] * n for i in range(n)]
def dfs(y, n, arr):

    if y==n-1:
        return arr
    for i in range(n):
        for j in range(n):
            for attr in arr:
                if i == attr[0] or j == attr[1]:
                    continue
                else:
                    arr.append((i,j))
                    return(dfs(i,n,arr))


for i in range(n):
    tmp = input()
    for j in range(n):
        if ord(tmp[j]) > 64 :
            board[i][j] = (ord(tmp[j]) - 64) * -1
        else:
            board[i][j] = int(tmp[j])

paths = []
for i in range(n):
    paths.append(dfs(0,n,[(0,i)]))

answer = []
for path in paths:
    ans = 1
    for attr in path:
        ans *= board[attr[0]][attr[1]]
    answer.append(ans)

print(answer)



