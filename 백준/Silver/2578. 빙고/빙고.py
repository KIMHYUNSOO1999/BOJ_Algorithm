import sys
input = sys.stdin.readline

def checkVisited(target, x, y):
    
    for i in range(5):
        for j in range(5):
            if arr[i][j] == target:
                visited[i][j] = True
                return
                
def lineVisited(line):
    for v in line:
        if not v:
            return False
    return True

def countVisited():

    cnt = 0

    for row in visited:
        if lineVisited(row):
            cnt += 1

    for col in zip(*visited):
        if lineVisited(col):
            cnt += 1

    diag1 = [visited[i][i] for i in range(5)]
    if lineVisited(diag1):
        cnt += 1

    diag2 = [visited[i][4 - i] for i in range(5)]
    if lineVisited(diag2):
        cnt += 1

    return cnt >= 3
    
arr = []
for _ in range(5):
    arr.append(list(map(int,input().rstrip().split())))

visited = [[False for _ in range(5)] for _ in range(5)]

order = []
for _ in range(5):
    order.append(list(map(int,input().rstrip().split())))

result=0
flag= True

for i in range(5):
    if flag == False:
        break
    for j in range(5):
        checkVisited(order[i][j],i,j)
        result+=1
        if countVisited():
            flag = False
            break
       
print(result)

