NUM = input()

CNT = 0 
for i in range(len(NUM)-1):
    if NUM[i] != NUM[i+1]:
        CNT += 1

print((CNT+1)//2)