dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


cnt = 1
x=0
y=0
num = 1
d = 0
dcnt= 1

r1,c1,r2,c2 = map(int, input().split())
arr = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
total = (c2-c1+1)*(r2-r1+1)

while(total > 0):
    if r1 <= x <= r2 and c1 <= y <= c2:
        arr[x-r1][y-c1] = num
        total -= 1
        m = num
    cnt += 1
    num += 1
    y = y+dy[d]
    x = x+dx[d]
    if cnt == dcnt:
        cnt = 0
        d = (d+3)%4
        if d==0 or d==2:
            dcnt += 1

max_len = len(str(m))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(arr[i][j]).rjust(max_len), end=" ")
    print()
