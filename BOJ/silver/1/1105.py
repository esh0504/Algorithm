L, R = map(str, input().split())

def Sol(l, r):
    cnt = 0

    if len(l) != len(r):
        return 0

    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                cnt += 1
        else:
            break

    return cnt

print(Sol(L,R))
