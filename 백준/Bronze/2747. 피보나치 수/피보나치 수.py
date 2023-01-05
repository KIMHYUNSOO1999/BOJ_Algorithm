list_fibonacci={0:0,1:1}
N=int(input())

for i in range(2,N+1):
    list_fibonacci[i]=list_fibonacci[i-1]+list_fibonacci[i-2]     
    
print(list_fibonacci[N])