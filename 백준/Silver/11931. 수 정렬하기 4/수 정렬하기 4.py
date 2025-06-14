import sys
input = sys.stdin.readline

n = int(input().strip())

arr=[]
for _ in range(n):
    arr.append(int(input().strip()))

arr.sort(reverse=True)

for w in arr:
    print(w)