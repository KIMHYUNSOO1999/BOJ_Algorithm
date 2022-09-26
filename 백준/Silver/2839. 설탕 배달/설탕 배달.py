CNT=0

N=int(input())

while(N>=0):
    if N%5==0:
        CNT+=N //5
        print(CNT)
        break
    N-=3
    CNT+=1
else:
    print('-1')