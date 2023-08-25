def solution(numbers, k):
    
    cnt=1
    i=0
    answer=0
    
    while numbers:
        if cnt==k:
            answer=i
            break
        
        if (i+2)<=len(numbers)-1:
            i+=2
            cnt+=1
        else:
            if (len(numbers)-1)-i==1:
                i=0
                cnt+=1
            else:
                i=1
                cnt+=1

    return numbers[answer]