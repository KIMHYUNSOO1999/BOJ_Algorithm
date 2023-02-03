import sys
input=sys.stdin.readline

arr = list(input().rstrip())

arr.sort(reverse=True)
result = 0

for i in arr:
    result += int(i)
    
if result % 3 != 0 or "0" not in arr:
    print(-1)
else:
    print(''.join(arr))