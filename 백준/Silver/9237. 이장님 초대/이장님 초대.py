import sys
input = sys.stdin.readline

n = int(input())
days = list(map(int, input().strip().split()))

days.sort(reverse=True)

max_days = 0
for i in range(n):
    max_days = max(max_days, days[i] + i)

print(max_days + 2)