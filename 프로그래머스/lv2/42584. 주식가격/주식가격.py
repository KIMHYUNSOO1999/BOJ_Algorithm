from collections import deque

def solution(prices):
    answer = []
    prices=deque(prices)
    
    while len(prices)>0:
        cur=prices.popleft()
        cnt=0
        
        for i in prices:
            cnt+=1
            if cur>i:
                break
                
        answer.append(cnt)
        
    return answer