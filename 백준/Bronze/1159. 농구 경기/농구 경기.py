CNT={}
word=''
Result=''

N=int(input())

for i in range(N):
    word=input()
    
    if CNT.get(word[0])==None:
        CNT[word[0]]=1
    else:
        CNT[word[0]]+=1

CNT = dict(sorted(CNT.items()))

for i in CNT:
    if CNT[i]>=5:
        Result+=str(i)

if Result=='':
    print('PREDAJA')
else:
    print(Result)
    