def fibo(n):
    if n==0:
        DP[n]=0
        return DP[n]
    elif n ==1:
        DP[n]=1
        return DP[n]
    else:
        if DP[n]>0:
            return DP[n]
        else:
            DP[n]=fibo(n-1)+fibo(n-2)
            return DP[n]
testCase=int(input())
for i in range(testCase):
    n=int(input())
    
    if n==0:
        print("1 0")
    elif n==1:
        print("0 1")
    else:
        DP=[0 for x in range(n+1) ]
        DP[0]=0
        DP[1]=1

        fibo(n)
        print(DP[n-1],DP[n])
