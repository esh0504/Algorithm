a=input()
b=len(a)

for i in range(0,b):
    if i==0:
        print(a[i],end='')

    elif i%10==9:
        print(a[i])
    else:
        print(a[i],end='')