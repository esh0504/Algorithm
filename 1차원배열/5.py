a=[]
for i in range(5):
    b=int(input())
    if b<40:
        b=40
    a.append(b)
sum=0
for k in range(len(a)):
    sum+=a[k]

print(int(sum/5))