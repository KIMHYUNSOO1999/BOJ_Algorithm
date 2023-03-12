def solution(hp):
    
    CNT=0

    while True:
        if hp<=0: break
        
        if (hp-5)>=0:
            hp-=5
            CNT+=1        
        elif (hp-3)>=0:
            hp-=3
            CNT+=1
        else:
            hp-=1
            CNT+=1
            
    return CNT