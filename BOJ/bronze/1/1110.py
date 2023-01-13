a = int(input())
b = [0] * 4
b[0] = a // 10
b[1] = a % 10
cnt = 0
while True:
    cnt += 1
    b[2] = (b[0] + b[1]) // 10
    b[3] = (b[0] + b[1]) % 10
    if a // 10 == b[1] and a % 10 == b[3]:
        break
    b[0] = b[1]
    b[1] = b[3]
print(cnt)


