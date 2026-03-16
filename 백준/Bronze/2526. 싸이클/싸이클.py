import sys
input = sys.stdin.readline

N, P = map(int, input().split())
arr = []
a = N

while True:
    a = (a * N) % P
    if a in arr:
        print(len(arr) - arr.index(a))
        break
    arr.append(a)