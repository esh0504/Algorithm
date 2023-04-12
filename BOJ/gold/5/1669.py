import sys
sys.stdin=open('input.txt')


x, y = map(int, input().split())
diff = y-x
add_height = 1


if diff <= 3:
    print(diff)
else:
    diff -= 3
    num = [1,1,1]
    while(diff != 0):
        for i in range(1,len(num)):
            if num[-i] == num[-i-1]:
                if  max(num) == num[-i] and num[-i-1] > num[-i-2]:
                    num.append(1)
                    break
                num[-i-1] = num[-i-1]+1
                break

        else:
            num.append(1)
        diff -= 1
    print(num)
    print(len(num))