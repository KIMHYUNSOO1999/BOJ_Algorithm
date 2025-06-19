import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr.sort()
for w in arr:
    if b>=w:
        b+=1

print(b)
