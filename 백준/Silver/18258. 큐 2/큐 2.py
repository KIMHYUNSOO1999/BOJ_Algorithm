from collections import deque
import sys
input = sys.stdin.readline

def push(x):
    arr.append(x)

def pop():
    if arr:
        print(arr.popleft())
    else:
        print(-1)

def size():
    print(len(arr))

def empty():
    if arr:
        print(0)
    else:
        print(1)

def front():
    if arr:
        print(arr[0])
    else:
        print(-1)

def back():
    if arr:
        print(arr[-1])
    else:
        print(-1)


arr = deque([])
n = int(input().rstrip())

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "front":
        front()    
    elif command[0] == "back":
        back()    
    