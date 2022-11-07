import sys
input = sys.stdin.readline
 
while True:
    
    stack = []
    flag = True
    texts=""
    toggle=0
    
    while(True):
        if toggle==1:break
        text=input().rstrip()
        for row in text:
            if row=='.':
                texts+=row
                toggle=1
                break
                
            texts+=row

    if texts == ".": break

        
    for row in texts:
        if row == '(' or row == '[':
            stack.append(row)
    
        elif stack and (row == ')' or row == ']'):  
            if row == ')' and stack[-1] == '(':
                stack.pop()
            elif row == ']' and stack[-1] == '[':
                stack.pop()
            else:    
                flag = False

        elif not stack and (row == ')' or row == ']'):  
            flag = False

    if flag and not stack:
        print('yes')
    else:
        print('no')