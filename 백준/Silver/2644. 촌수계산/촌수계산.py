import sys
input=sys.stdin.readline

def dfs(dx,CNT):
    CNT+=1
    
    visited[dx]=True
    
    if dx==y:
        result.append(CNT)
    
    for i in graph[dx]:
        if not visited[i]:
            dfs(i,CNT)
            
N=int(input())

x,y=map(int,input().rstrip().split(' '))

n=int(input())

graph = [[] for _ in range(N+1)]

for _ in range(n):
  a, b = map(int, input().split())  
  graph[b].append(a)
  graph[a].append(b)
        
visited = [False] * (N+1)

result=[]

dfs(x,0)

if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)