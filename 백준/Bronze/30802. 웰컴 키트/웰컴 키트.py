import sys
input = sys.stdin.readline

people = int(input())
arr = list(map(int,input().split()))
stdA,stdB = map(int,input().split())

# Tshirt

answer=0
for size in arr:
    answer+=(size+stdA-1)//stdA
    
print(answer)

# pen

tmpA= people//stdB
tmpB= people%stdB

print(tmpA, tmpB)