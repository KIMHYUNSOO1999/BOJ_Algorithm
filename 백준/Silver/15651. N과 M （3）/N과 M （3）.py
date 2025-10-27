import sys
input = sys.stdin.readline

def dfs(arr,tmpArr,M):
    if len(tmpArr) == M:
        print(" ".join(map(str, tmpArr)))
        return

    for i in range(len(arr)):
        tmpArr.append(arr[i])
        dfs(arr,tmpArr,M)
        tmpArr.pop()

N, M = map(int, input().rstrip().split())
arr = [i for i in range(1,N+1)]
dfs(arr,[],M)