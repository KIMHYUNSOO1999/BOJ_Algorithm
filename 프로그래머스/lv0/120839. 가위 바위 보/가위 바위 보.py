def solution(rsp):
    
    Rock_Paper_Scissors={'0':'5','2':'0','5':'2'}
    
    answer = ''
    
    for i in str(rsp):
        answer+=Rock_Paper_Scissors[i]
        
    return ''.join(answer)