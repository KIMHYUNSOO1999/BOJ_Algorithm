import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque()
q.append(N)

visited = [-1] * 100001
visited[N] = 0

while q:

    x = q.popleft()

    if x == K:
        print(visited[x])
        break

    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i <= 100000 and visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)