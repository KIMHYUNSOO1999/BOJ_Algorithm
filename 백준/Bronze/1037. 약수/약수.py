while(True):
    check=0
    
    N=int(input())  
    number=list(map(int, input().split()))
    
    for i in range(0,N):
        if int(number[i]) <= 1000000:
            check+=1
    
    number=list(set(number))
        
    if N<50 and check==N: break
      
number_max = max(number)
number_min = min(number)

print(number_max * number_min)