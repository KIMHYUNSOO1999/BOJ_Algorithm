def solution(a):
    answer = 0
    
    if a[0]>=0 and a[1]>=0:
        answer=1
    elif a[0]<=0 and a[1]>=0:
        answer=2
    elif a[0]<=0 and a[1]<=0:
        answer=3
    else:
        answer=4
        
    return answer