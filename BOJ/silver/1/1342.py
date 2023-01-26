import sys

sys.stdin = open('../../gold/5/input.txt')

testCase = int(input())


def str2dict(s):
    answer = {}
    for i in range(len(s)):
        if s[i] not in answer:
            answer[s[i]] = 1
        else:
            answer[s[i]] += 1
    return answer

def Sol(pre, l):
    answer = 0
    if l == len(S):
        return 1

    for k in s_dict.keys():
        if k == pre or s_dict[k] == 0:
            continue
        s_dict[k] -= 1
        answer += Sol(k, l + 1)
        s_dict[k] += 1
    return answer


for _ in range(testCase):



    S = input()
    s_dict = str2dict(S)
    print(Sol('', 0))

