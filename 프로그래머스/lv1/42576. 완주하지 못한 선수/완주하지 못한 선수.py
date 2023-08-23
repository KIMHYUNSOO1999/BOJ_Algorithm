from collections import Counter

def solution(participant, completion):
    
    participant=Counter(participant)
    completion=Counter(completion)
    
    temp=participant-completion
    
    answer=list(temp.keys())[0]
    
    return answer