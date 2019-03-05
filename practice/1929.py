import math

m,n=map(int,input().split())

num=int(math.sqrt(n))

list=[]
listcopy=[]
a=[]
acopy=[]
answer=[]

for i in range(m,n+1):
    list.append(i)

for i in range(2,num+1):
    a.append(i)

while (len(a)!=0):
    answer.append(a[0])
    acopy=[]
    listcopy=[]
    for i in range(len(list)):
        if list[i]%a[0]!=0:
            listcopy.append(list[i])
    for i in range(len(a)):
        if a[i]%a[0]!=0:
            acopy.append(a[i])

    list=listcopy
    a=acopy

for i in range(len(answer)):
    if answer[i]>=m:
        print(answer[i])
for i in range(len(list)):
    if list[i]!=1:
        print(list[i])