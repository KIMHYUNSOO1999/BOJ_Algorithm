def solution(nums):
    nums_tmp=set(nums)
    cnt=len(nums)//2
    
    if cnt>len(nums_tmp):
        answer=len(nums_tmp)
    else:
        answer=cnt
    
    return answer