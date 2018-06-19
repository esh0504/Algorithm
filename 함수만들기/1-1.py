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
I