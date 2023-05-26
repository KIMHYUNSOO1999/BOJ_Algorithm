def solution(n):
    
    answer = [0 for _ in range(n+1)]
    answer[1]=1

    for i in range(2,n+1):
        answer[i]=answer[i-1]+answer[i-2]
        
    return answer[-1]%1234567