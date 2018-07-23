def self_numb(input_numb):
    res = input_numb
    for i in range(len(str(input_numb))):
        res += int(str(input_numb)[i])
    return res


tf = [0] * 10001
for i in range(1, 10000):
    if tf[i] == 0:
        j = i
        while True:
            j = self_numb(j)

            if j >= 10000:
                break
            tf[j] = 1

for i in range(1, 10000):
    if tf[i] == 0:
        print(i)