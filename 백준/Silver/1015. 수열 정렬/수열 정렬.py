import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

sorted_with_index = sorted((val, idx) for idx, val in enumerate(arr))

rank = [0] * n
for order, (_, idx) in enumerate(sorted_with_index):
    rank[idx] = order

print(*rank)