import sys
input = sys.stdin.readline
s = input().strip()
N = len(s)

R, C = 0, 0
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        R = i
        C = N // i

matrix = [[''] * C for _ in range(R)]

idx = 0
for c in range(C):
    for r in range(R):
        matrix[r][c] = s[idx]
        idx += 1

result = []
for r in range(R):
    for c in range(C):
        result.append(matrix[r][c])

print(''.join(result))