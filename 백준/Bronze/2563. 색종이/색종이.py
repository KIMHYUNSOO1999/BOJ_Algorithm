import sys
input=sys.stdin.readline

square = [[0 for _ in range(100)] for _ in range(100)]

N= int(input())

for _ in range(N):
    a,b=map(int,input().split(" "))
    
    for i in range(a,a+10):
        for j in range(b,b+10):
            square[i][j]=1

CNT=0

for row in square:
    CNT+=row.count(1)

print(CNT)