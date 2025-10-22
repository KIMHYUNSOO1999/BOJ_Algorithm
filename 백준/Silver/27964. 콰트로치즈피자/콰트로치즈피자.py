import sys
input = sys.stdin.readline

n = int(input())
arr = set(i for i in input().split() if i[-6:]=='Cheese')
print('yummy' if len(arr) >= 4 else 'sad')