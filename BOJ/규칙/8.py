a=int(input())
b=[]
c=str(a)
count2=0
for i in range(len(c)):
    b.append(int(c[i]))
    if b[i]==6 or b[i]==9:
        b[i]=9
        count2+=1
if count2%2==0:
    count2=int(count2//2)

else:
    count2=int(count2//2)+1


b.append(10)
b.sort()
count=1
lscount=[]
lscount.append(count2)

for k in range(count2):
    b.remove(9)


for t in range(len(c)-count2):
        if b[t]==b[t+1]:
            count=count+1
        else:
            lscount.append(count)
            count=1


lscount.sort()
print(lscount.pop())
