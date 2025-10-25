import sys
input = sys.stdin.readline

def dfs(idx, arr, result):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(idx+1, len(arr)):
        result.append(arr[i])
        dfs(i, arr, result)
        result.pop()
    
N, M = map(int, input().rstrip().split())
arr = [i for i in range(1, N+1)]

for i in range(len(arr)):
    dfs(i, arr, [arr[i]])