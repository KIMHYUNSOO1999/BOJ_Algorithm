import sys
input=sys.stdin.readline

N, K = map(int, input().rstrip().split())
arr=list(map(int, input().rstrip().split()))

arr.sort(reverse=False)

print(arr[K-1])