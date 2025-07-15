import sys
input = sys.stdin.readline

n, k = map(int,input().rstrip().split())

arr = [[1 for _ in range(i+1)] for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

print(arr[n-1][k-1])