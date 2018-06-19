a=int(input())
average=0
e=0

for i in range(a):
    b=list(map(int,input().split()))
    e=0
    for k in range(1,b[0]+1):
        average=average+b[k]
    average=average/b[0]
    for t in range(b[0]):
        if b[t+1]>average:
            e=e+1

    n=float(e/b[0]*100)
    print('%.3f' %n,end='')
    print('%')

    average=0



