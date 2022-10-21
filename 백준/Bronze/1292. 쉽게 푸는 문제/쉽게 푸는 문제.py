import sys
input = sys.stdin.readline

A,B = map(int,input().split())
 
Array = [0]

for i in range(46):
    for j in range(i):
        Array.append(i)
 
print(sum(Array[A:B+1]))