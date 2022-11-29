import sys
input=sys.stdin.readline

N=int(input())

for _ in range(N):
    nums=[]
    nums=list(map(int, input().split(" ")))
    nums.sort()
    print(nums[-3])