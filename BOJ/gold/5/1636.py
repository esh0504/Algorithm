import sys
sys.stdin = open('./input.txt')

n = int(input())

life = 0
curr_stress = 0
ran = []
for i in range(n):
    s, e = map(int,input().split())
    ran.append((s,e))
answer = []
for i in range(-1, n-1):
    if i==-1:
        if ran[i+2][0] > ran[i+1][1]:
            curr_stress = ran[i+1][1]
        else:
            if ran[i+1][0] > ran[i+2][1]:
                curr_stress = ran[i+1][0]
            else:
                curr_stress = ran[i+2][0]
        answer.append(curr_stress)
        continue
    old_stress = curr_stress
    if ran[i+1][0] <= curr_stress <= ran[i+1][1]:
        answer.append(curr_stress)
        continue
    else:
        if ran[i+1][0] > curr_stress:
            curr_stress = ran[i+1][0]
        else:
            curr_stress = ran[i+1][1]

    life += abs(curr_stress - old_stress)
    answer.append(curr_stress)

print(life)
for attr in answer:
    print(attr)