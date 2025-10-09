import itertools
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

result = set()
for e in list(itertools.permutations(arr,k)):
    result.add(''.join(map(str, e)))

print(len(result))