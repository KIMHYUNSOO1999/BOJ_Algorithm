while(True):
    N=int(input())
    if 1<=N<=100: break
         
for i in range(1,N+1):
    print(" "*(i-1) + "*"*(N-i+1))