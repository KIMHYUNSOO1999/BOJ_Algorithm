import sys
input = sys.stdin.readline

def dfs(x,y,visited,arr):

    dx = [1,0]
    dy = [0,1]

    for i in range(2):
        
        ddx=x+dx[i]
        ddy=y+dy[i]

        if 0<=ddx<m and 0<=ddy<n and visited[ddx][ddy]==False and arr[ddx][ddy]==1:
            visited[ddx][ddy] = True
            dfs(ddx,ddy,visited,arr)
            
        
n, m = map(int,input().strip().split())

arr=[]
for _ in range(m):
    arr.append(list(map(int,input().strip().split())))

visited=[[False for _ in range(n)] for _ in range(m)]

if arr[0][0] == 1:
    visited[0][0] = True
    dfs(0, 0, visited, arr)

if visited[m-1][n-1]:
    print("Yes")
else:
    print("No")