number=[0,0,0,0,0,0,0,0,0,0]
A=int(input())
B=int(input())
C=int(input())

N=str(A*B*C)

for i in range(len(N)):
    number[int(N[i])]+=1
    
for row in number:
    print(row)