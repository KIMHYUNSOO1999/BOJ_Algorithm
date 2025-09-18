import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().rstrip().split()))

numset = set(numbers)
a = list(numset)
a.sort()

numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i

for i in numbers:
    print(numdict[i], end=' ')