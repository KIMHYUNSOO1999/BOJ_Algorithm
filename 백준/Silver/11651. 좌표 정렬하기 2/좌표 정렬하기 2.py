import sys
input = sys.stdin.readline

cnt = int(input())

arr = []
for i in range(cnt):
    tmpA,tmpB = map(int,input().split(' '))
    arr.append((tmpA, tmpB))  

for answer in sorted(arr, key=lambda x:(x[1],x[0])):
    print(answer[0], answer[1])