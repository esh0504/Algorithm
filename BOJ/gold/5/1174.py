import sys

sys.stdin = open('input.txt')

arr = []
results = set()

def Sol():
    if len(arr) > 0:
        results.add(int("".join(map(str, arr))))
    for i in range(0, 10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            Sol()
            arr.pop()

n = int(input())

Sol()
results = list(results)
results.sort()
if len(results) < n:
    print(-1)
else:
    print(results[n-1])

