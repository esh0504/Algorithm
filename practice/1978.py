num=int(input())

a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()
count=0
for k in range(num):
    print(count)
    for i in range(2,a[num-1]):
        if a[k]==1:
            break
        if a[k]==i:
            count+=1
            break

        elif a[k]-1==i:
            count+=1
            break
        
        elif a[k]%i==0:
            break

        elif a[k]<=i:
            count+=1
            break
print(count)
## 틀렸습니다.
