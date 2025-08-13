import sys
input = sys.stdin.readline

N, newScore, P = map(int,input().split())
rank = sorted(list(map(int,input().split())) + [newScore], reverse=True)

result = {}
tmpRank = 1
tmpCount = 0

if N == P and rank[-1] >= newScore:
    print(-1)
else:
    for r in rank:
        
        if r not in result:  
            result[r] = tmpRank
            
        tmpRank+=1
        tmpCount+=1
        if tmpCount >= P:  
            break
            
    print(result[newScore])
