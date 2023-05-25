def solution(s):
    
    stack=[]
    
    for word in s:
        if word=="(":
            stack.append(word)
        elif len(stack) and word==")":
            stack.pop()
        else:
            return False
        
    if stack:
        return False
    
    return True