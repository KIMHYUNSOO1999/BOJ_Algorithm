import sys
input=sys.stdin.readline

def dfs(x,y,arr):
    
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False

    k=arr[x][y]

    if visited[x][y]==0:
        visited[x][y]=1
        dfs(x+k,y,arr)
        dfs(x,y+k,arr)
        return True

N=int(input())

graph=[]
visited = [[0 for j in range(N)] for i in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
    
dfs(0,0,graph)

if visited[N-1][N-1]==1:
    print("HaruHaru")
else:
    print("Hing")