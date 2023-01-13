a=int(input())
b=0
for i in range(1,10000001):
    b=b+i
    c=i+1
    d=b-a

    if b>=a:
        if b>=a:
            if i%2==1:
                print("%d/%d" %(d+1,c-d-1))
                break
            else:
                print("%d/%d"%(c-d-1,d+1))
                break