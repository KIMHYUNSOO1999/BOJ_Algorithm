word_list=[]

while(True):
    word=str(input())
    if 3<=len(word)<=50: break

for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        for k in range(j+1, len(word)):
            row = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            word_list.append(row)

word_list.sort()
print(word_list[0])