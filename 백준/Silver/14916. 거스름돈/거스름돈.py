import sys
input = sys.stdin.readline

N = int(input())

CNT = 0

while(True):
    if N % 5 == 0:   
        CNT += N//5		
        break
    else:
        N -= 2    
        CNT += 1

    if N < 0:   
        break
if N<0:			
    print(-1)			
else:
    print(CNT)