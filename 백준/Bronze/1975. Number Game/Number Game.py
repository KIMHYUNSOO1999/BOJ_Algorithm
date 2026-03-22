import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    
    N = int(input().rstrip())
    answer = 0

    for i in range(2, N+1):
        x = i   
    
        while x <= N:
            if N % x == 0:
                answer += 1
                x *= i  
            else:
                break
   
    print(answer)