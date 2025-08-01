import sys
input = sys.stdin.readline

def gcd(a, b):

    while b>0:
        a, b = b, a%b

    return a
    
def pairs(arr):
    
    tmpArr = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tmpArr.append((arr[i], arr[j]))
            
    return tmpArr
    
t = int(input().rstrip())

for _ in range(t):
    
    arr = list(map(int, input().rstrip().split()))[1:]
    
    answer=0
    for i, j in pairs(arr):
        answer+=gcd(i,j)
        
    print(answer)