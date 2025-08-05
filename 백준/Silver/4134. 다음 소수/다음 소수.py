import sys
input = sys.stdin.readline

def minDecimal(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

n = int(input().rstrip())

for _ in range(n):
    
    order = int(input().rstrip())
    
    while True:
        
        if order in [0, 1]:
            print(2)
            break
            
        if minDecimal(order):
            print(order)
            break
        else:
            order+=1