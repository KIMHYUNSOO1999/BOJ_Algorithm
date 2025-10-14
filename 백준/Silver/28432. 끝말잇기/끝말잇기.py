import sys
input = sys.stdin.readline

n = int(input())
arr = []
cnt = -1
for i in range(n):
    tmp = input().rstrip()
    if tmp == '?': cnt = i
    arr.append(tmp)

m = int(input())
words = [input().rstrip() for _ in range(m)]

left = arr[cnt - 1][-1] if cnt > 0 else None
right = arr[cnt + 1][0] if cnt < n - 1 else None

for w in words:
    if (w not in arr) and ((left is None or w[0] == left)) and ((right is None or w[-1] == right)):
        print(w)
        break