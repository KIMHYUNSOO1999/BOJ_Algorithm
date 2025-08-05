import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
arr = [int(input()) for _ in range(n)]

length = [arr[i+1] - arr[i] for i in range(n - 1)]

sub = length[0]
for i in range(1, len(length)):
    sub = gcd(sub, length[i])

result = 0
for l in length:
    result += l // sub - 1

print(result)
