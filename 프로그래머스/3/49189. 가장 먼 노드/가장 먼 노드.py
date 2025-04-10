from collections import deque

def solution(n, edge):
    
    edge = sorted(edge)  
    distance = [0] * (n+1) 
    queue = deque()
    graph = [[] for _ in range(n+1)]
    answer = 0
    
    for i in edge:  
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    queue.append(1)  
    distance[1]=1  
    
    while queue:
        current = queue.popleft()
        for node in graph[current]:
            if distance[node] == 0: 
                queue.append(node) 
                distance[node] = distance[current] + 1 

    max_distance = max(distance)  
    for j in distance:
        if j == max_distance:
            answer += 1
            
    return answer