import sys
input = sys.stdin.readline

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

n: int = int(input())

for _ in range(n):
    a: int
    b: int
    a, b = map(int, input().rstrip().split())
    print(lcm(a, b))