import sys
input=sys.stdin.readline

def dfs(x,y,N):
    
    if len(N)==6:
        if N not in result:
            result.append(N)
        return
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    for i in range(4):
        
        ddx=x+dx[i]
        ddy=y+dy[i]
        
        if 0<=ddx<5 and 0<=ddy<5:
            dfs(ddx,ddy,N+graph[ddx][ddy])
            
graph=[]
result=[]

for _ in range(5):
    graph.append(list(map(str, input().rstrip().split())))
    
for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])
        
print(len(result))