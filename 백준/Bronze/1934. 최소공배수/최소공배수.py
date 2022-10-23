import sys
input=sys.stdin.readline

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    result = A*B

    while B>0:
        A,B = B, A%B

    print(result//A)