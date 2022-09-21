numbers=[]
flag=0
a=0
b=0

for i in range(9):
    numbers.append(int(input()))
    
for i in range(len(numbers)):
    if flag==1:
        break
    for j in range(i+1,len(numbers)):
        if sum(numbers)-(numbers[i]+numbers[j])==100:
            a,b=i,j
            flag=1
            break
if b>a:
    del numbers[b]
    del numbers[a]
else:
    del numbers[a]
    del numbers[b]

for row in sorted(numbers):
    print(row)