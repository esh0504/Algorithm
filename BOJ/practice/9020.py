testCase=int(input())
def isPrime():
    ls=[]
    a=20000
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
answer=isPrime()
for i in range(testCase):
    num=int(input())
    mid=int(num/2)
    if mid in answer:
        print(mid,mid)
    else:
        for k in range(mid,0,-1):
            max=num-k
            if max in answer and k in answer:
                print(k,max)
                break

    
    