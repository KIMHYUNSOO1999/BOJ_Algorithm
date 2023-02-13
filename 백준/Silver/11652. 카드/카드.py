import sys
input = sys.stdin.readline

N=int(input().rstrip())

arr={}

for i in range(N):
    num=int(input().rstrip())
    if arr.get(num)==None:
        arr[num]=1
    else:
        arr[num]+=1
        
result = sorted(arr.items(),key=lambda x:(-x[1],x[0]))

print(result[0][0])