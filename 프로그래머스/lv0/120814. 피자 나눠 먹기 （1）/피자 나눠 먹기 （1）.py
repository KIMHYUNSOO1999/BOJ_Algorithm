def solution(n):
    
    answer=1
    
    while True:
        if n>answer*7:
            answer+=1
        else:
            break
            
    return answer