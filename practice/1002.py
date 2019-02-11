testCase=int(input())
for i in range(testCase):
    x1,y1,r1,x2,y2,r2=map(int,input().split())

    d=(((y2-y1)**2)+((x2-x1)**2))**0.5
    d1=r1+r2
    d2=((r2-r1)**2)**0.5
    if x1==x2 and y1==y2:
        if r1==r2:
            count=-1
        else:
            count=0
    else:
        if d1<d:
            count=0
        elif d1==d:
            count=1
        else:
            if d2==d:
                count=1
            elif d2>d:
                count=0
            else:
                count=2

    print(count)