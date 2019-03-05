import math

m,n=map(int,input().split())

num=int(math.sqrt(n))

a=[]
acopy=[]
d=[]
dcopy=[]
answer=[]
for i in range(m,n+1):
    a.append(i)

for i in range(2,num+1):
    d.append(i)

while(len(d)!=0):
    dcopy=[]
    for i in range(len(a)):
        if a[i]%d[0]!=0:
            acopy.append(a[i])
        else:
            continue
    for i in range(len(d)):
        answer.append(d[i])
        if d[i]%d[0]!=0:
            dcopy.append(d[i])
        else:
            continue

    a=acopy
    d=dcopy

for i in range(len(answer)):
    print(answer[i])