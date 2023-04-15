import sys
sys.stdin = open('./input.txt')

testCase = int(input())

def dfs(n):
    try:
        if dp[n] != 0:
            return dp[n]
        dp[n] = dfs(n//p) + dfs(n//q)
        return dp[n]
    except:
        dp[n] = 0
        if dp[n] != 0:
            return dp[n]
        dp[n] = dfs(n//p) + dfs(n//q)
        return dp[n]

for _ in range(testCase):
n, p, q = map(int,input().split())
dp = {0:1}

print(dfs(n))