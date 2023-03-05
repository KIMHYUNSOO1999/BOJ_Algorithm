def solution(slice, n):
    answer=1
    
    while True:
        
        tmp=answer*slice
        
        if tmp<n:
            answer+=1
        else:
            break
            
    return answer