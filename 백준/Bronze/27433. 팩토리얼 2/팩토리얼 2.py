import sys
input = sys.stdin.readline

def dfs(n):

    if n == 0:
        return 1

    return n * dfs(n-1)

n = int(input().rstrip())
print(dfs(n))

