count_list=[]
N=int(input())

for _ in range(N):
    
    CNT=0
    word=input()

    for i in range(len(word)):
        if word[i]=='O':
            if word[i]==word[i-1] and i!=0:
                check+=1
                CNT+=check
            else:
                check=1
                CNT+=check
        else:
            check=0
            
    count_list.append(CNT)
    
for row in count_list:
    print(row)