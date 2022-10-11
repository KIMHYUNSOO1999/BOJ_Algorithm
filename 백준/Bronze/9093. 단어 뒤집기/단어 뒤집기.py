N=int(input())

word_result=[]

for _ in range(N):
    word=input().split(' ')
    word_temp=[]
    for row in word:
        word_temp.append(row[::-1])
    word_result.append(" ".join(word_temp))
    
for answer in word_result:
    print(answer)