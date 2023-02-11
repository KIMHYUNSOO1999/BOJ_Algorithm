import sys
input = sys.stdin.readline

A,B=map(str,input().rstrip().split(' '))

CNT=1
toggle=0

while True:
    if int(A)==int(B) or toggle==1 or int(A)>int(B): break
        
    if B[len(B)-1]=='1':
        B=B[0:len(B)-1]
    elif int(B)%2==0:
        B=str(int(B)//2)
    else:
        toggle=1
        break
        
    CNT+=1

if toggle==1 or int(A)>int(B):
    print(-1)
else:
    print(CNT)
    