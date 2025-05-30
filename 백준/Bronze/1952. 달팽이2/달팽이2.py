import sys
input = sys.stdin.readline

x, y = map(int, input().strip().split())

arr = [1]

for i in range(1,y):
    arr.append(2*i)

if x>y:
    print(arr[-1]+1)
else:
    print(arr[x-1])
