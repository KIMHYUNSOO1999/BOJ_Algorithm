import sys
input = sys.stdin.readline

cnt, search = map(int, input().split())

medal=[]
for i in range(cnt):
    tmp=list(map(int,input().split()))
    medal.append(tmp)

medal = sorted(medal, key = lambda x : (-x[1],-x[2],-x[3]))

result = 0
tmp = 0
for i in range(len(medal)):
    
    if i!=0 and (medal[i][1] == medal[i-1][1]) and (medal[i][2] == medal[i-1][2]) and (medal[i][3] == medal[i-1][3]):
        tmp += 1
    else:
        result+=(tmp+1)
        tmp = 0

    if medal[i][0] == search:
        break

print(result)
        