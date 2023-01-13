test_case=int(input())

for i in range(test_case):
    flour=int(input())
    ho=int(input())
    num=[]
    num.clear()

    for f in range(0,flour):
        if f==0:
            for h in range(1,ho+1):
                num.append(h)
        else:
            for k in range(1,ho):
                num[k]=num[k-1]+num[k]

    a=0

    for j in range(ho):
        a=a+num[j]


    print(a)