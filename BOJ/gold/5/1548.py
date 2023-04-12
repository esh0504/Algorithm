import sys
sys.stdin=open('input.txt')

testCase = int(input())

def check_trinangle(arr):
    if len(arr) < 3:
        return len(arr)
    if arr[0]+arr[1]<=arr[-1]:
        return -1
    return len(arr)

for _ in range(testCase):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max_len = 1
    for x in range(len(arr)):
        for z in range(x+1,len(arr)):
            max_len = max(max_len, check_trinangle(arr[x:z+1]))
    print(max_len)

