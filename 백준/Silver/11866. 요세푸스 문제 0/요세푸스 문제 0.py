N, K = map(int,input().split())
Result_list= []
nums_list = [i for i in range(1,N+1)] 
num = 0

for i in range(N):
    
    num+=(K-1)
    if num >= len(nums_list):
        num %= len(nums_list)
    Result_list.append(str(nums_list[num]))
    nums_list.pop(num)


print("<",', '.join(Result_list),">", sep="")