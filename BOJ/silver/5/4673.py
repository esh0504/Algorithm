def d (num):
    a=[]
    nonself=0
    for i in range(len(str(num))):
        a.append(str(num)[i])

    for k in range(len(a)):
        nonself=nonself+int(a[k])

    nonself+=num

    return nonself

c=[]
for i in range(1,10000):
    c.append(d(i))

c.sort()

c=list(set(c))
b=[]
for k in range(1,10000):
    b.append(k)

for j in range(len(c)):
    if c[j] in b:
        b.remove(c[j])

for u in range(len(b)):
    print(b[u])