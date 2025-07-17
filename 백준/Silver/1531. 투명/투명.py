import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

visited = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            visited[i][j] += 1

result = 0
for i in range(1, 101):
    for j in range(1, 101):
        if visited[i][j] > M:
            result += 1

print(result)