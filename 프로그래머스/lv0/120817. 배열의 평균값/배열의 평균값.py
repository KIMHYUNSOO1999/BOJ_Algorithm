def solution(numbers):
    
    CNT=0
    
    for i in range(len(numbers)):
        CNT+=numbers[i]
        
    return CNT/len(numbers)