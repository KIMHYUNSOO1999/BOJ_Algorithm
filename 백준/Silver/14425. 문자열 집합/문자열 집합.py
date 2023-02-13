import sys
input = sys.stdin.readline

N,M=map(int,input().rstrip().split(' '))

S = set([input() for _ in range(N)])
CNT = 0

for _ in range(M):
    a = input()
    if a in S:
        CNT += 1
        
print(CNT)