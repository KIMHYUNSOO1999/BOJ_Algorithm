import sys
input = sys.stdin.readline

def dfs(n):

    if n <= 1:
        return n

    return dfs(n-1) + dfs(n-2)

n = int(input().rstrip())
print(dfs(n))

