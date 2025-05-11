import sys
input = sys.stdin.readline

N, L, D = map(int, input().split())

time = [0]
for i in range(1, N * 2):
    if i % 2 == 1:
        time.append(time[i - 1] + L)
    else:
        time.append(time[i - 1] + 5)

tmp = 0
while True:
    tmp += D 

    for i in range(0, len(time), 2): 
        start = time[i]
        end = time[i + 1]
        if start <= tmp < end:
            break  
    else:
        print(tmp)
        break
