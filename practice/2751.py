#파이썬이라 시간초과 나는듯 함 mergy sort 사용해씀

def stls(ls1,ls2):
    left=int(0)
    ls=[]
    right=int(0)
    while left<len(ls1) and right<len(ls2):
        if ls1[left]>=ls2[right]:
            ls.append(ls1[left])
            left+=1
        elif ls1[left]<ls2[right]:
            ls.append(ls2[right])
            right+=1
    if left==len(ls1):
        for i in range(right,len(ls2)):
            ls.append(ls2[i])
    elif right==len(ls2):
        for i in range(left,len(ls1)):
            ls.append(ls1[i])
    return ls

num=int(input())
ls=[]
for i in range(num):
    a=[]
    b=int(input())
    a.append(b)
    ls.append(a)
while len(ls)!=1:
    aa=[]
    if len(ls)%2==1:
        ls[0]=stls(ls[0],ls[-1])
        ls.pop()
    for i in range(0,len(ls)-1,2):
        aa.append(stls(ls[i],ls[i+1]))
    ls=aa
    
for i in range(len(ls[0])):
    print(ls[0][i])

