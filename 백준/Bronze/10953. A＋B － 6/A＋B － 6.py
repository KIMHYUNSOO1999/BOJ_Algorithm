N=int(input())
result=[]

for i in range(N):
    question=list(map(int,input().split(',')))
    result.append(question[0]+question[1])
    
for word in result:
    print(word)