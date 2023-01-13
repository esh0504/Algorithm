import sys
input = sys.stdin.readline

N = int(input())

straw=[]
for _ in range(N):
    straw.append(int(input()))

straw.sort(reverse=True)



res=0
for i in range(len(straw)-2):
    if straw[i] < straw[i+1] + straw[i+2]:
        res = straw[i] + straw[i+1] + straw[i+2]
        break
    else:
        res=-1

print(res)