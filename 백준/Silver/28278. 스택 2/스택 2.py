import sys
input = sys.stdin.readline

def stack1(stack, x):
    stack.append(x)

def stack2(stack):
    if stack:
        print(stack.pop())
    else:
        print(-1)

def stack3(stack):
    print(len(stack))

def stack4(stack):
    if stack:
        print(0)
    else:
        print(1)

def stack5(stack):
    if stack:
        print(stack[-1])
    else:
        print(-1)
    
n = int(input().rstrip())

stack = []
for _ in range(n):

    command = list(map(int, input().strip().split()))

    if command[0] == 1:
        stack1(stack,command[1])
    elif command[0] == 2:
        stack2(stack)
    elif command[0] == 3:
        stack3(stack)
    elif command[0] == 4:
        stack4(stack)
    elif command[0] == 5:
        stack5(stack)

