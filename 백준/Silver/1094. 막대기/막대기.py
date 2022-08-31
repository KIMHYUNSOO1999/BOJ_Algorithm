range=64
stick=0
count=0

while(True):
    X=int(input())
    if X<=64: break
        
while range >= 1: 
    if stick + range > X:
        pass
    else:
        stick+=range
        count+=1
        
    range=int(range/2)
        
        
print(count)