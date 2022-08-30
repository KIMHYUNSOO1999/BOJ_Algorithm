import math

T=int(input())
count=T

while(True):
    if count==0:
        break
        
    N, M = map(int, input().split(' '))
    if (0<=N<=29) and (1<=M<=30) and N<=M:
        print(math.comb(M, N))
        count=count-1