a=int(input())
b=[]
c=str(a)
for i in range(len(c)):
    b.append(int(c[i]))
    if b[i]==6:
        b[i]=9

b.append(10)
b.sort()
count=1
lscount=[]

for t in range(len(c)):
        if b[t]==b[t+1]:
            count=count+1
        else:
            lscount.append(count)
            count=1


lscount.sort()
print(lscount.pop())


#6과 9를 바꾸는 방법 생각해야함
