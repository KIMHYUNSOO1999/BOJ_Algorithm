def wordSameTwo(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt == 1

def dfs(begin, target, words, visited, depth):
    
    global answer
    
    if begin == target:
        answer = depth
        return
    
    for i in range(len(words)):
        if not visited[i] and wordSameTwo(begin, words[i]):
            visited[i] = True
            dfs(words[i], target, words, visited, depth + 1)
            visited[i] = False
    
def solution(begin, target, words):
    
    global answer
    
    visited = [False for _ in range(len(words))]
    
    if target in words:
        dfs(begin, target, words, visited, 0)
    else:
        answer=0
                
    return answer