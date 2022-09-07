N=list(map(int,input().split(' '))) 

A=N[0]
B=N[1]

for _ in range(N[2]):
    A=(A%B)*10
   
print(int(A/B))