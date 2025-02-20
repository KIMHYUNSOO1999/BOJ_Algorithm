import sys
input = sys.stdin.readline

_, cnt2 = map(int, input().split())

arr=[0]
arr += list(map(int,input().split()))

for i,num in enumerate(arr):
    if i!=0:
        arr[i]=arr[i-1]+num

for _ in range(cnt2):
    tmpA, tmpB =map(int,input().split())
    print(arr[tmpB] - arr[tmpA-1])