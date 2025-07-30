def dfs(begin, t, tmp, visited, depth):
    
    if depth == maxTicket:
        answer.append(tmp[:])
        return 
    
    if begin not in t:  
        return
    
    for i in range(len(t[begin])):
        
        if not visited[begin][i]:
            
            tmp.append(t[begin][i])
            visited[begin][i] = True
            
            dfs(t[begin][i], t, tmp, visited, depth + 1)
                 
            tmp.pop()
            visited[begin][i] = False
        
def solution(tickets):
    
    global answer
    answer = []
    
    global maxTicket
    maxTicket = len(tickets)
    
    t = {}
    for start, end in tickets:
        if start not in t:
            t[start] = []
        t[start].append(end)
           
    visited = {}
    for key in t:
        t[key].sort()
        visited[key] = [False] * len(t[key])
            
    dfs("ICN", t, ["ICN"], visited, 0)
    
    return answer[0]