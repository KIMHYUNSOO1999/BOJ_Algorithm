import sys
input = sys.stdin.readline

arr=[1]

def factorial(n1):
    for i in range(1, n1+1):
        arr.append((arr[i-1] * i) % 1234567891)

N, K = map(int,input().split())
factorial(max(N,K))

print(arr[N]//(arr[K]*arr[N-K]))