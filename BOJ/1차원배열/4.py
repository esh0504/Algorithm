a=(input())
b=a.split()

count=0
for i in range(1,len(b)):
    if b[i]>b[i-1]:
        count+=1


if count==0:
    print("descending")
elif count==7:
    print("ascending")
else:
    print("mixed")
