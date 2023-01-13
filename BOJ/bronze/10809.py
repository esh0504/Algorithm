a=input()
aList=[]
for k in range(len(a)):
    aList.append(a[k])
b=[]
for i in range(97,123):
    b.append(chr(i))
result=""

for i in range(len(b)):

    if b[i] in aList:
        result+=str(aList.index(b[i]))+" "
    else:
        result+="-1 "
print(result)