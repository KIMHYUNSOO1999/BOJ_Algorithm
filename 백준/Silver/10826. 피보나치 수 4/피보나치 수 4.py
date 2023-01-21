import sys
input = sys.stdin.readline

arr = [0, 1, 1]

for i in range(3, 10001):
    arr.append((arr[i - 2]) + arr[i - 1])

N = int(input())
print(arr[N])