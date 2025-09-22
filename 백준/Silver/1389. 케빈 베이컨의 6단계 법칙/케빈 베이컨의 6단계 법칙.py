import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, start, N):
    num = [0] * (N+1)
    ch = [0] * (N+1)
    ch[start] = 1
    Q = deque([start])

    while Q:
        x = Q.popleft()
        for i in graph[x]:
            if ch[i] == 0:
                num[i] = num[x] + 1
                ch[i] = 1
                Q.append(i)

    return sum(num)

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A].append(B)
    graph[B].append(A)

answer = [BFS(graph, i, N) for i in range(1, N+1)]
print(answer.index(min(answer)) + 1)