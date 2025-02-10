import sys
input = sys.stdin.readline

length = int(input())
alpha = input().strip()

std='abcdefghijklmnopqrstuvwxyz'

answer=0
for i in range(length):
    answer+=(std.index(alpha[i])+1)*(31**i) 

print(answer % 1234567891)