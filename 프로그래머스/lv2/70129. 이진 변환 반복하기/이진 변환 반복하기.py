def solution(s):
    
    CNT=0
    CNT2=0
    while True:
        if s=='1': break
        
        tmp=0
        
        for num in s:
            if num=='0':
                CNT+=1
            else: tmp+=1
            
        s=format(tmp, 'b')
        
        CNT2+=1
        
    return [CNT2,CNT]
    