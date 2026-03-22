import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    
    N = int(input().rstrip())
    answer = 0

    for i in range(2,N+1):
        tmpN = N
    
        while tmpN:
            tmpN,tmpA = tmpN//i, tmpN%i
            if tmpA==0:
                answer+=1
            else:
                break
   
    print(answer)