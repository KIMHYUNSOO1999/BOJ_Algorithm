import sys
input=sys.stdin.readline

def number_square(number, square):   
    return sum([int(i) ** square for i in str(number)])

def dfs(A,B,visited,cnt):
    if visited[A]:
        return visited[A]-1
    
    visited[A]=cnt
    
    temp = number_square(A, B)
    
    cnt+=1
    return dfs(temp,B,visited,cnt)
    
visited = [0] * 250000
A,B=map(int,input().split(' '))
answer=dfs(A,B,visited,1)
print(answer)