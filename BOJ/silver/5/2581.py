mini=int(input())
max=int(input())
sum=0
answer=[]
for i in range(mini,max+1):
    if i==2 or i==3 or i==5 or i==7:
        sum+=i
        answer.append(i)
    else:
        for k in range(3,(i//2)+1):
            if i%k==0:
                break
            elif k==(i//2):
                sum+=i
                answer.append(i)

if sum==0:
    print("-1")
else:
    print(sum)
    print(answer[0])
