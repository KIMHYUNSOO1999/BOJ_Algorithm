import sys
input = sys.stdin.readline

cnt, std= map(int,input().split())

arr=[]
for _ in range(cnt):
    arr.append(int(input()))

arr.sort()
start, end = 1, arr[-1]

while start <= end:
    
    mid = (start+end)//2
    line=0

    for i in arr:
        line += i // mid

    if line >= std:
        start = mid+1
    else:
        end = mid-1

print(end)
    