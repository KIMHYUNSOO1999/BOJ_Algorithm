def solution(n):
    answer=1
    
    while True:
        
        tmp=answer*6
        
        if tmp%n!=0:
            answer+=1
        else:
            break
            
    return answer