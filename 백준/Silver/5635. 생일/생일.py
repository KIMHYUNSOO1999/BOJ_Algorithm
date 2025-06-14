import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    
    tmp = list(input().strip().split())
    tmp[1]=int(tmp[1])
    tmp[2]=int(tmp[2])
    tmp[3]=int(tmp[3])
    
    arr.append(tmp)

arr = sorted(arr, key = lambda x:(x[3],x[2],x[1]))

print(arr[-1][0])
print(arr[0][0])