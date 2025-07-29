def dfs(idx, computers, visited, n):
    
    visited[idx] = True
    for i in range(n):          
        if i != n and computers[i][idx] == 1 and visited[i] == False:    
                dfs(i, computers, visited, n)       

def solution(n, computers):
    
    answer = 0
    visited = [False for _ in range(n)] 
    
    for idx in range(n):
        if visited[idx] == False:  
            dfs(idx, computers, visited, n)
            answer += 1
            
    return answer