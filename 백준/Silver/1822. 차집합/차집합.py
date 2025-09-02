import sys
input = sys.stdin.readline

n, m = map(int, input().split())
aArr = set(map(int, input().split()))
bArr = set(map(int, input().split()))

result = sorted(aArr - bArr)  

if result:
    print(len(result))
    print(" ".join(map(str, result)))
else:
    print(0)
