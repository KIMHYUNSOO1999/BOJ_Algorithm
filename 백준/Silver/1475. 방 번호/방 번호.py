N = input()
max_value=0
count=[0,0,0,0,0,0,0,0,0,0]

for row in N:
    row = int(row)
    
    if row == 6:
        row = 9
    
    count[row] += 1
        
if count[9]%2==0:
    count[9]=(int(count[9]/2))
else:
     count[9]=(int(count[9]/2)+1)

print(max(count))