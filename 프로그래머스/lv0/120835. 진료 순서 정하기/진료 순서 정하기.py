def solution(emergency):
    standard={}
    
    temp=sorted(emergency,reverse=True)

    for i in range(len(temp)):
        standard[temp[i]]=i+1
        
    for i in range(len(emergency)):
        emergency[i]=standard[emergency[i]]
        
    return emergency