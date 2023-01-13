a,b,c=map(int,input().split())

if a>b>c:
    print(b)
elif b>a>c:
    print(a)
elif c>a>b:
    print(a)
elif c>b>a:
    print(b)
elif a>c>b:
    print(c)
elif b>c>a:
    print(c)
elif a==b==c:
    print(a)
elif a==b>c:
    print(a)
elif a>b==c:
    print(b)
elif c>b==a:
    print(b)
elif c==b>a:
    print(b)
elif b>a==c:
    print(a)
elif b==a>c:
    print(a)
elif c>a==b:
    print(a)
elif c==a>b:
    print(a)
elif a>c==b:
    print(c)
elif a==c>b:
    print(c)
elif b>c==a:
    print(c)
else:
    print(c)