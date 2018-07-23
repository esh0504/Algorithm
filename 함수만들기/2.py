def hansu(N):
    count=0
    for i in range(1,N+1):
        num=str(i)
        if len(num)==1:
            count+=1
        elif len(num)==2:
            count+=1
        elif len(num)==3:
            d=int(num[0])-int(num[1])
            if d==int(num[1])-int(num[2]):
                count+=1
            else:
                continue
    return count
a=int(input())
print(hansu(a))

