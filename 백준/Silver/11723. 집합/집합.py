import sys
input=sys.stdin.readline

cnt = int(input())

S = set()
for i in range(cnt):

    # input
    tmp = input().strip().split()
    if len(tmp) == 1:
        a = tmp[0]
    else:
        a, b = tmp[0],int(tmp[1])

    # to-do
    if a == "add":
        
        S.add(b)
        
    elif a == "remove":

        if b in S:
            S.remove(b)
                
    elif a == "check":

        if b in S:
            print(1)
        else:
            print(0)
            
    elif a == "toggle":
        
        if b in S:
            S.remove(b)
        else:
            S.add(b)
            
    elif a == "all":
        
        S = set([ i for i in range(1,21)])
        
    elif a == "empty":
        
        S = set()

