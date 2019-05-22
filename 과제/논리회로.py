def solution(input):

    ##�Է°��� �������� �޾Ƴ���
    size=int(input[0])
    numofmin=int(input[1])
    minar=[]
    for i in range(2,len(input)):
        min=int(input[i])
        minb=""
        minb2=""
        for i in range(size):
            if(min%2==1):
                minb+="1"
            else:
                minb+="0"
            min=min//2
        for i in range(size):
            minb2+=minb[size-i-1]
        minar.append(minb2)

    minar2=[]
    ##��ġ��
    while(True):
        for i in range(numofmin):  
            for k in range(numofmin):
                cnt=0
                cnt2=0
                min1=minar[i]
                min2=minar[k]
                mink=""
                for i in range(size):
                    if min1[i]==min2[i]:
                        mink+=min1[i]
                    else:
                        cnt+=1
                        mink+="-"
                        if cnt>1:
                            break
                if size==len(mink):
                    minar2.append(mink)
                    cnt2+=1
                else:
                    continue
        
        minar=minar2
        minar2=[]
        if cnt2==0:
                    break
    answer=minar
    return answer

input=[3, 6, 0, 1, 2, 5, 6, 7]
print(solution(input))