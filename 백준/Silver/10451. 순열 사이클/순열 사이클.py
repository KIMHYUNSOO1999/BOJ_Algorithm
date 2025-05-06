def dfs(start, visited):
    next = dic[start]
    if not visited[next]:
        visited[next] = True
        dfs(next, visited)

T = int(input())
for _ in range(T):
    
    N = int(input())
    input_list = list(map(int, input().split()))
    
    dic = {i+1: input_list[i] for i in range(N)}
    visited = [False] * (N + 1) 

    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            dfs(i, visited)
            count += 1
            
    print(count)