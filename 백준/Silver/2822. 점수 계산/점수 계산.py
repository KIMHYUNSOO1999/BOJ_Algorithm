score_list=[]
temp_list={}
Result_list=[]

for i in range(8):
    score_tmp=int(input())
    score_list.append(score_tmp)
    temp_list[score_tmp]=i+1
    
score_list.sort(reverse=True)
Result_score=sum(score_list[0:5])

for high_score in score_list[4::-1]:
        Result_list.append(temp_list[high_score])
Result_list.sort()

print(Result_score)
for num in Result_list:
    print(num,end=' ')