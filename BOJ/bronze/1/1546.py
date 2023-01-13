a=int(input())#시험수
average=0
b=list(map(int,input().split()))
b.append(0)
c=0

for i in range(a):

    if c>int(b[i]):
        c=c
    else:
        c=int(b[i])
for k in range(a):

    b[k]=b[k]/c*100

for t in range(a):

    average=b[t]+average

average=average/a

print(average)




