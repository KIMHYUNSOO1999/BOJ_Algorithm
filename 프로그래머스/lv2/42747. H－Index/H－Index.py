def solution(citations):
    citations=sorted(citations,reverse=True)
    
    for idx,i in enumerate(citations):
        print(idx,i)
        if idx >= i:
            return idx
        
    return len(citations)