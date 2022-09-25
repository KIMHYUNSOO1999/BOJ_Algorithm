CNT_list=[]
N=int(input())

for _ in range(N):
    score=list(map(int,input().split(" ")))
    sum_score=0
    
    for row in score[1:len(score)]:
        sum_score+=row
        
        CNT_a=0
        CNT_sum=0
        
    for row in score[1:len(score)]:
        if row>sum_score/score[0]:
            CNT_a+=1   
    CNT_list.append((CNT_a/score[0])*100)

for row in CNT_list:
    print(f'{row:.3f}%')