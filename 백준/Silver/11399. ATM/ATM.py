import sys
input=sys.stdin.readline 

N=int(input())

numbers=list(map(int,input().split(" ")))
numbers.sort()

CNT=0

for i in range(len(numbers)):
    CNT+=numbers[i]
    for j in range(0,i):
        CNT+=numbers[j]
     
print(CNT)