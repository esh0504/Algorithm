a=input()

b=["dz=","c=","c-","d-","lj","nj","s=","z="]
count=0
while len(a)!=0:
    for i in b:
        if a[:len(i)] in b:
            count+=1
            a=a[len(i):]
            break
        if i=="z=":
            count+=1
            a=a[1:]
            break
print(count)
