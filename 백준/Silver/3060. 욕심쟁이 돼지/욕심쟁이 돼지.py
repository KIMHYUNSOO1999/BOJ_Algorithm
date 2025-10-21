import sys
input = sys.stdin.readline

cnt = int(input())
for _ in range(cnt):
    
    N = int(input())
    pig = list(map(int,input().rstrip().split()))
    result = 1
    
    while N  >= sum(pig):
        tmp = [0]*6
        for i in range(len(pig)):
            if i == len(pig)-1:
                tmp[i]= pig[i-1]+pig[i]+pig[(i+1)%6]+pig[(i+3)%6]
            else:
                tmp[i]= pig[i-1]+pig[i]+pig[(i+1)%6]+pig[(i+3)%6]
        pig = tmp
        result+=1

    print(result)