import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(dx,depth):
    visited[dx]=True

    for i in graph[dx]:
        if not visited[i]:
            dfs(i,depth+1)
            
N,M= map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())  
    graph[b].append(a)
    graph[a].append(b)

visited = [False] * (1+N)
CNT=0

for i in range(1,N+1):
    if not visited[i]:
        if not graph[i]:  
            CNT+=1 
            visited[i]=True  
        else:  
            dfs(i, 0)  
            CNT+=1  
        
print(CNT)