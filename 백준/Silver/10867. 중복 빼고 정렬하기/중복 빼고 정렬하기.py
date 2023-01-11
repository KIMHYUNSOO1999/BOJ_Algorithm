N= int(input())

nums_list=[]

nums_list=list(set(list(map(int,input().split(' ')))))
nums_list.sort()

for num in nums_list:
    print(num,end=' ')