def solution(record):
    
    answer = []
    dic = {}
    
    for s in record:
        sTmp = s.split()
        if len(sTmp) == 3:
            dic[sTmp[1]] = sTmp[2]
            
    for s in record:
        sTmp = s.split()
        
        if sTmp[0] == 'Enter':
            answer.append(f'{dic[sTmp[1]]}님이 들어왔습니다.')
        elif sTmp[0] == 'Leave':
            answer.append(f'{dic[sTmp[1]]}님이 나갔습니다.')
            
    return answer