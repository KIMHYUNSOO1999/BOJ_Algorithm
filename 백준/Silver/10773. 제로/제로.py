import sys
input=sys.stdin.readline 

N = int(input())
nums = []

for i in range(N):
    number = int(input())
    if number == 0:
        nums.pop()
    else:
        nums.append(number)
        
print(sum(nums))