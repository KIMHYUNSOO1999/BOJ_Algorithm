from collections import deque
import sys
input = sys.stdin.readline

def setFront(x):
    d.appendleft(x)
    return

def set(x):
    d.append(x)
    return

def getFront():
    if d:
        print(d.popleft())
    else:
        print(-1)
        
    return

def get():
    if d:
        print(d.pop())
    else:
        print(-1)

    return

def count():
    print(len(d))
    return

def empty():
    if d:
        print(0)
    else:
        print(1)
    
def get2Front():
    if d:
        print(d[0])
    else:
        print(-1)

    return

def get2():
    if d:
        print(d[-1])
    else:
        print(-1)

    return

        
n = int(input().rstrip())
d = deque()

for _ in range(n):
    
    order = list(map(int,input().rstrip().split()))

    if order[0] == 1:
        setFront(order[1]) 
    elif order[0] == 2:
        set(order[1]) 
    elif order[0] == 3:
        getFront() 
    elif order[0] == 4:
        get()
    elif order[0] == 5:
        count() 
    elif order[0] == 6:
        empty()
    elif order[0] == 7:
        get2Front() 
    elif order[0] == 8:
        get2()
