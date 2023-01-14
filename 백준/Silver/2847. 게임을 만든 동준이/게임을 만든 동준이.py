N=int(input())
score=[]

for _ in range(N):
    score.append(int(input()))
    
CNT=0

for i in range(N-1,0,-1):
    if score[i] <= score[i-1]:
        CNT +=(score[i-1]-score[i]+1)
        score[i-1]=score[i]-1
    
print(CNT)