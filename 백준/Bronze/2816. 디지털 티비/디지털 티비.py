import sys
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]
r = []

i = a.index("KBS1")
for _ in range(i):
    r.append('1')
for j in range(i, 0, -1):
    a[j], a[j-1] = a[j-1], a[j]
    r.append('4')

i = a.index("KBS2")
for _ in range(i):
    r.append('1')
for j in range(i, 1, -1):
    a[j], a[j-1] = a[j-1], a[j]
    r.append('4')

print(''.join(r))