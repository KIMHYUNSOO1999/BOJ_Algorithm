ESM=list(map(int,input().split(' ')))
CNT=1


a=1
b=1
c=1

while(True):
    
    if ESM[0]==a and ESM[1]==b and ESM[2]==c: break
        
    if a>=15:
        a=1
    else:
        a+=1
    
    if b>=28:
        b=1
    else:
        b+=1

    if c>=19:
        c=1
    else:
        c+=1
    
    CNT+=1
    
print(CNT)
    