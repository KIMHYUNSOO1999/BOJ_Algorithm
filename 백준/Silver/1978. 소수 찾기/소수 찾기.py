import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
CNT = 0

for x in data:
  for i in range(2, x+1):
    if x % i == 0:
      if x == i:
        CNT += 1
      
      break

print(CNT)