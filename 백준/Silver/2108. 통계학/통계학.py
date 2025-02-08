import sys
input = sys.stdin.readline

cnt = int(input())

arr = []
for i in range(cnt):
    arr.append(int(input()))
arr.sort()

# 1 
print(round(sum(arr)/len(arr)))

# 2
print(arr[len(arr)//2])

# 3
dic = {}
for val in arr:
    if val not in dic:
        dic[val]=1
    else:
        dic[val]+=1

nums = []
for k, v in dic.items():
    if v == max(dic.values()):
        nums.append(k)

nums.sort()
print(nums[1]) if len(nums)>1 else print(nums[0])

# 4
print(max(arr)-min(arr))