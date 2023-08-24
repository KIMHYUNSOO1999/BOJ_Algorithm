from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer=0
    bridge=deque([0]*bridge_length)
    truck_weights=deque(truck_weights)
    
    sum_bridge=0
    while len(bridge)>0:
        
        answer += 1
        tmp=bridge.popleft()
        sum_bridge-=tmp
        
        if truck_weights:
            if sum_bridge + truck_weights[0] <= weight:
                tmp=truck_weights.popleft()
                bridge.append(tmp)
                sum_bridge+=tmp
            else:
                bridge.append(0)
                 
    return answer