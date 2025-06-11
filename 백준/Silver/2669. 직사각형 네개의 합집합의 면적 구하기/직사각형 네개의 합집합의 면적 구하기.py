import sys
input = sys.stdin.readline

visited = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    x_start, x_end = min(x1, x2), max(x1, x2)
    y_start, y_end = min(y1, y2), max(y1, y2)
    
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            visited[i][j] = 1

print(sum(row.count(1) for row in visited))
