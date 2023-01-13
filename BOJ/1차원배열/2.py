a=int(input())
b=int(input())
c=int(input())
result=a*b*c
result=str(result)
for i in range(10):
    count=0
    for j in range(len(result)):

        if i==int(result[j]):
            count+=1
    print(count)
