import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

result = ""
total_dist = 0

for col in range(m):
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    
    for row in range(n):
        count[arr[row][col]] += 1

    best = min(count.keys(), key=lambda x: (-count[x], x))
    result += best
    total_dist += n - count[best]

print(result)
print(total_dist)
