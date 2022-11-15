import sys
input=sys.stdin.readline

def Rev(num):
    num=str(num)
    num_reverse=''
    for row in num[::-1]:
        num_reverse+=row
    
    return int(num_reverse)
        
X,Y=map(int,input().split(" "))
print(Rev(Rev(X)+Rev(Y)))
        
        