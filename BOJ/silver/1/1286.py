import sys

sys.stdin = open('input.txt')

testCase = int(input())


for _ in range(testCase):
    answer = [0 for i in range(26)]
    N, M = map(int,input().split())
    arr = []
    for row in range(N):
        freq = (row+1) * (2*N-row) + (row+N+1) * (N-row)
        word=input()
        for col in range(M):
            freq_r = (col+1) * (2*M-col) + (col+M+1) * (M-col)
            answer[ord(word[col])-65] += (freq * freq_r)
    for frequency in answer:
        print(frequency)

