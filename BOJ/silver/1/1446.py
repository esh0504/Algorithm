import sys
sys.stdin = open('./input.txt')

testCase = int(input())

for _ in range(testCase):
    arr = []
    n, total_d = map(int,input().split())
    dp = [0 for i in range(total_d + 1)]
    for i in range(n):
        start,end,dist = map(int,input().split())
        arr.append((start,end,dist))
    arr = sorted(arr, key= lambda x: x[1])
    # print(arr)
    arr_idx = 0
    for i in range(1,total_d + 1):
        dp[i] = dp[i - 1] + 1
        if arr_idx < n:
            while (arr[arr_idx][1] == i):
                dp[i] = min(dp[i], dp[arr[arr_idx][0]] + arr[arr_idx][2])
                arr_idx += 1
                if arr_idx >= n:
                    break
    print(dp[total_d])

