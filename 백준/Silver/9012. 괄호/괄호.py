from collections import deque
import sys
input=sys.stdin.readline

def stack(st):
    cnt=0
    tmp=[]
    while st:
        i=st.popleft()
        if i==')' and '(' not in tmp:
            return 'NO'
        elif i=='(':
            tmp.append(i)
        else:
            tmp.pop(0)
       
    if len(tmp)>0:
        return 'NO'
    else:
        return 'YES'
    
cnt=int(input().strip())
answer=[]
for i in range(cnt):
    exam=deque(input().strip())
    answer.append(stack(exam))
    
for i in answer:
    print(i)