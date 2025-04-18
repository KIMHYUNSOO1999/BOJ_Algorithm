def solution(files):
    
    answer = []
    for f in files:
        
        head, number, tail = '', '', ''

        flag = False
        for i in range(len(f)): 
            
            if f[i].isdigit():  
                number += f[i]
                flag = True
            elif not flag:  
                head += f[i]
            else:               
                tail = f[i:]
                break
                
        answer.append((head, number, tail))  

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  

    return [''.join(t) for t in answer]   