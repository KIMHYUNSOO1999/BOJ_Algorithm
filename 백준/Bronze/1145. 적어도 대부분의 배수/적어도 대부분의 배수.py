number=list(map(int,input().split(' ')))
    
number_min=min(number)
    
while(True):
    count=0
    for i in range(len(number)):
        if number_min%number[i]==0:
            count+=1

    if count > 2:
        print(number_min)
        break
            
    number_min+=1