def solution(genres, plays):
    tmp_list=[]
    answer=[]
    
    for i in range(len(plays)):
        tmp_list.append((genres[i],plays[i],i))
    tmp_list=sorted(tmp_list,key=lambda x:(x[0],-x[1],x[2]))
    
    tmp_dict={}
    for i in tmp_list:
        if i[0] not in tmp_dict:
            tmp_dict[i[0]]=i[1]
        else:
            tmp_dict[i[0]]+=i[1]
    
    tmp_dict2=sorted(tmp_dict.items(),key=lambda x:-x[1])
    
    for i in tmp_dict2:
        CNT=0
        for j in tmp_list:
            if CNT==2:
                break
            elif i[0]==j[0]:
                CNT+=1
                answer.append(j[2])
    
    return answer