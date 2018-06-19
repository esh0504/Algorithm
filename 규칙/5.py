num=int(input())
for i in range(num):
    h,w,n=map(int,input().split())
    if n%h==0:
        H=str(h)
    else:
        H=str(n%h)

    W=n/h
    if int(W)<W:
        W=int(W+1)
        W=str(W)
    else:
        W=int(W)
        W=str(W)

    if int(W)<10:
        W="0"+W

    print(H+W)