import sys
input=sys.stdin.readline

N=int(input())

arr=[]
result=[]

CNT=1
flag=0

for _ in range(N):
    num=int(input())
    while(CNT<=num):
        arr.append(CNT)
        result.append('+')
        CNT+=1
        
    if arr[-1]==num:
        arr.pop()
        result.append('-')
    else:
        print('NO')
        flag=1
        break
            
if flag == 0:
    for i in result:
        print(i)