import sys

N=int(sys.stdin.readline())
answer_compare=set(map(int, sys.stdin.readline().split(" ")))

M=int(sys.stdin.readline())
answer=list(map(int, sys.stdin.readline().split(" ")))
    
for i in range(len(answer)):
    if answer[i] in answer_compare:
        print('1')
    else:
        print("0")