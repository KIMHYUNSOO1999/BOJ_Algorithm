N=int(input())

CNT=0 
i=0
subtotal=""

while(True):
    
    sum_CNT=0
    subtotal=str(CNT)
    
    sum_CNT+=CNT
    
    for word in subtotal:
        i=int(word)
        sum_CNT+=i
        
    if sum_CNT==N:
        break
    elif CNT==N:
        CNT=0
        break
        
    CNT+=1
    
print(CNT)

    
