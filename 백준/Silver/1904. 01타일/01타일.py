import sys
input = sys.stdin.readline

N=int(input())

arr=[0]*1000001

arr[0]=1
arr[1]=2

for i in range(2,N+1):
    arr[i]=(arr[i-1]+arr[i-2])%15746
    
print(arr[N-1])