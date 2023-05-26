def solution(n):
    a=format(n,'b').count('1')

    n+=1

    while True:
        tmp=format(n,'b')
        if tmp.count('1')==a: break
        n+=1
        
    return n