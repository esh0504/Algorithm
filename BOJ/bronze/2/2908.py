a, b = map(int, input().split())


def bak(a):
    return int(int(a) / 100) * 100


def sip(a):
    return int(int(a - bak(a)) / 10) * 10


def ill(a):
    return a - (bak(a)) - (sip(a))


num1 = (ill(a) * 100) + (sip(a)) + int(bak(a) / 100)
num2 = (ill(b) * 100) + (sip(b)) + int(bak(b) / 100)
if num1 > num2:
    print(num1)
else:
    print(num2)