import sys
input = sys.stdin.readline

n = int(input())
c = input().rstrip()

ev = False
result=[]
for i in range(0,len(c),n):
    tmp = c[i:i+n]
    if ev == False: 
        result.append(list(tmp))
        ev= True
    else:
        result.append(list(tmp[::-1]))
        ev = False

rows = len(result)
cols = len(result[0])

answer=''
for col in range(cols):
    for row in range(rows):
        answer += result[row][col]

print(answer)