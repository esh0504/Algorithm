a=int(input())

if a%5==0:
    print(a//5)
elif a==1:
    print(-1)
elif a==2:
    print(-1)
elif a==4:
    print(-1)
elif a==7:
    print(-1)
elif a%5==1:
    print(((a-6)//5)+2)
elif a%5==2:
    print(((a-12)//5)+4)
elif a%5==3:
    print(((a-3)//5)+1)
elif a%5==4:
    print(((a-9)//5)+3)
else:
    print(-1)
