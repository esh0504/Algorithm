import sys
sys.stdin = open('./input.txt')

n = int(input())
arr = []
for i in range(n):
    t,s = map(int,input().split())
    arr.append((t,s))

arr = sorted(arr, key=lambda x: x[1])
start = sum = arr[0][1]-arr[0][0]
for attr in arr:
    sum += attr[0]
    while(sum > attr[1]):
        start -= 1
        sum -= 1

if start >= 0:
    print(start)
else:
    print(-1)
