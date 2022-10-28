keyword_list=[]

for _ in range(5):
    keyword_list.append(input())
    
result = ['' for i in range(15)]

for row in keyword_list:
    word=row
    for i in range(len(row)):
        if result[i]==None:
            result[i].append(word[i])
        else:
            result[i]+=word[i]
            
for row in result:
    if row != "":
        print(row,end="")