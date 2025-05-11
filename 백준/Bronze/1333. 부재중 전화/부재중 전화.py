import sys
input = sys.stdin.readline

N, L, D = map(int, input().split())

L+=5
num=0
time=D

for i in range(N):
    num+=L
    while True:
        if time<num-5:
            time+=D
        else:
            break
    if num-5<=time<num:
        break
        
print(time)