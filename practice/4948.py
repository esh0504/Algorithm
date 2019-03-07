m=int(input())

def isPrime():
    ls=[]
    a=246913
    answer=[]
    num=[]
    for i in range(1,a+1):
        ls.append(i)
    for i in range(2,497):
        num.append(i)
    while(len(num)!=0):
        answer.append(num[0])
        numcopy=[]
        lscopy=[]
        for i in range(len(ls)):
            if ls[i]%num[0]!=0:
                lscopy.append(ls[i])
        for i in range(len(num)):
            if num[i]%num[0]!=0:
                numcopy.append(num[i])
        ls=lscopy
        num=numcopy
    for i in range(len(ls)):
        answer.append(ls[i])
    return answer

def count(m,n):
    count=0
    test=[]
    for i in range(len(n)):
        if m>=n[i]:
            continue
        elif m<n[i] and 2*m>=n[i]:
            count+=1
            test.append(n[i])
        else:
            return test

n=isPrime()
print(n)
while(m!=0):
    print(count(m,n))
    
    m=int(input())
    
