import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
n, m = map(int,input().rstrip().split(':'))
a = gcd(n, m)
print(f"{n//a}:{m//a}")