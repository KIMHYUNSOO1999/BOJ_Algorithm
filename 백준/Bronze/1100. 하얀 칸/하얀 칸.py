CNT=0

for i in range(8):
    row=[]
    row=list(map(str, list(input())))
    
    if i%2==0:
        for j in [0,2,4,6]:
            if row[j]=='F':
                CNT+=1
    else:
        for k in [1,3,5,7]:
            if row[k]=='F':
                CNT+=1
print(CNT)