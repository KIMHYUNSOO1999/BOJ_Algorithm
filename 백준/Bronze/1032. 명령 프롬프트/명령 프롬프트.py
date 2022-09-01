word_list=[]
word=''

while(True):
    N=int(input())
    if N<=50: break

for i in range(0,N):
    i = str(input())
    word_list.append(i)
    
for j in range(len(word_list[0])):    
    temp=[]
    check=0
    for i in range(0,N):
        temp.append(word_list[i][j])
    
    search=temp[0]
    
    for i in range((len(temp))):
        if temp[i] in search:
            check+=1
    
    if check==N:
        word+=search
    else:
        word+='?'
        
print(word)