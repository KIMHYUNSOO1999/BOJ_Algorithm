import sys
input=sys.stdin.readline

N=int(input())
Sort_N=[]
for _ in range(N):
    Sort_N.append(int(input()))
    
Sort_N=list(set(Sort_N))
Sort_N.sort()

for row in Sort_N:
    print(row)