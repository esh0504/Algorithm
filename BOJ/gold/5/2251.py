import sys
sys.stdin = open('./input.txt')

a,b,c = map(int,input().split())
vox = [a,b,c]

direction = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
answer = set()
visited = []

def fill(x, y, i):
    new_v=x+y
    if new_v > vox[i]:
        return (new_v - vox[i],vox[i])
    else:
        return (0, new_v)
def dfs(arr):
    if arr[0] == 0:
        answer.add(arr[2])
    if arr[2] == c and (0, 0, c) in visited:
        return c;
    for dir in direction:
        next_a, next_b, next_c = arr[0],arr[1],arr[2]
        if dir[0] == 0:
            if dir[1] == 1:
                next_a, next_b = fill(arr[0],arr[1], 1)
            else:
                next_a, next_c = fill(arr[0],arr[2], 2)
        elif (dir[1] == 0):
            if dir[1] == 0:
                next_b, next_a = fill(arr[1],arr[0], 0)
            else:
                next_b, next_c = fill(arr[1],arr[2], 2)
        else:
            if dir[1] == 0:
                next_c, next_a = fill(arr[2],arr[0], 0)
            else:
                next_c, next_b = fill(arr[2],arr[1], 1)

        if (next_a, next_b, next_c) in visited:
            continue
        else:
            visited.append((next_a, next_b, next_c))
            dfs([next_a,next_b,next_c])

arr = [0,0,c]
dfs(arr)
answer = sorted(answer)
for attr in answer:
    print(attr, end=' ')