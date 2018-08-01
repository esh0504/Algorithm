import math

testcase=int(input())

for i in range(testcase):
    n,m=map(int,input().split())
    up=1
    down=1

    while n>0:
        up=m*up
        down=n*down
        m=m-1
        n=n-1

    print(int(up/down))


