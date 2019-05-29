##입력받은 함수를 이진수로 바꿔주는 함수
def chbinary(input):
    minar=[]
    for i in range(len(input)):
        num=int(input[i])
        c=""
        while(int(num/2)!=0):
            if(num%2==1):
                c="1"+c;
                num=int(num/2);
            else:
                c="0"+c;
                num=int(num/2);
        c=str(num)+c
        minar.append(c)
    minar=binarysize(minar)
    return minar

##리스트안의 이진수의 사이즈를 맞추는 함수
def binarysize(input):
    max=0
    for i in range(len(input)):
        if max<len(input[i]):
            max=len(input[i])
        else:
            continue
    for i in range(len(input)):
        if max>len(input[i]):
            c=input[i]
            while(max!=len(c)):
                c="0"+c
            input[i]=c
    return input

##한글자가 다르면 그 글자를 -로 바꾸는 함수
def merge(input):
    minar=[]
    epi=[]
    nepi=[]
    for i in range(len(input)):
        for j in range(len(input)):
            cnt=0
            cnt2=0
            c=""
            for k in range(len(input[0])):
                if input[i][k]!=input[j][k]:
                    cnt+=1
                if cnt>=2:
                    break;
                else:
                    continue
            if cnt==1:
                for k in range(len(input[0])):
                    if input[i][k]!=input[j][k]:
                        c+="-"
                    else:
                        c+=input[i][k]
                minar.append(c)
                cnt2+=1
            if cnt2==1 and j==len(input)-1:
                epi.append(c)
            elif cnt2>=2 and j==len(input)-1:
                nepi.append(c)
    epi2=epi
    nepi2=nepi
    epi=[]
    nepi=[]
    for i in range(len(epi2)):
        if epi2[i] in epi:
            continue
        else:
            epi.append(epi2[i])
    for k in range(len(nepi2)):
        if nepi2[i] in nepi:
            continue
        else:
            nepi.append(nepi2[i])
    minar=["epi"]
    for i in range(len(epi)):
        minar.append(epi[i])
    minar.append("nepi")
    for i in range(len(nepi)):
        minar.append(nepi[i])

    return minar
input=[3, 6, 0, 1, 2, 5, 6, 7]
print(merge(chbinary(input)))
