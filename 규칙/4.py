a=int(input())

for i in range(a):
    b=0
    x,y=map(int,input().split())
    distance=y-x
    for t in range(1,2**31):
        b=b+(t*2)
        if b>=distance:
            if b - t < distance:
                print(t*2)
                break
            else:
                print(t*2-1)
                break