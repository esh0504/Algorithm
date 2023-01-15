import sys
sys.stdin = open('input.txt')


def dfs(row, col, cnt):
    global answer
    check_arr[row][col] = 1
    for dir in directions:
        new_r = row + dir[1]
        new_c = col + dir[0]
        if row == 0 and col == C-1:
            if cnt == K:
                answer += 1
            return 0
        # Boundary Check
        if 0<=new_r<R and 0<=new_c<C and check_arr[new_r][new_c]==0 and arr[new_r][new_c]!='T':
            check_arr[new_r][new_c]=1
            dfs(new_r,new_c,cnt+1)
            # 다시 돌아와야하므로 check Flag를 0으로
            check_arr[new_r][new_c]=0


directions = [(1,0),(-1,0),(0,1),(0,-1)]
answer = 0

R, C, K = map(int,input().split())
check_arr = [[0 for col in range(C)] for row in range(R)]
arr = []
for i in range(R):
    map_ = input()
    arr.append(map_)
dfs(R-1, 0, 1)
print(answer)



