n=int(input())
a=1

for i in range(1,1000000000):

    a=(i*6)+a
    if n==1:
        print(n)
        break

    elif n<=a:
        print(i+1)
        break
    else:
        continue

