from collections import deque
import sys
input = sys.stdin.readline

def bfs(queue,visited):

    while queue:
        pos,jump=queue.popleft()
        for i in range(1,jump+1):
            if pos+i >= N or visited[pos+i]:
                continue
            visited[pos+i] = visited[pos]+1
            queue.append((pos+i,arr[pos+i]))
    
    
N=int(input())

if N == 1:
    print(0)
    sys.exit()
    
arr=list(map(int,input().rstrip().split(' ')))

visited = [False] * N

queue = deque([(0,arr[0])])
bfs(queue,visited)

print(visited[-1] if visited[-1] else -1)