def solution(num_list, n):
    
    answer=[]
    tmp=[]
    CNT=0

    for num in num_list:
        
        if CNT==n:
            answer.append(tmp)
            tmp=[]
            CNT=0
        elif num_list[-1]==num:
            answer.append(tmp)
            
        tmp.append(num)
        CNT+=1
    
    return answer