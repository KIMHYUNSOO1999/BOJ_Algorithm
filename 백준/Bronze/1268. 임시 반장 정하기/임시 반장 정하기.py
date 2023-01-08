N=int(input())

arr = [[0 for j in range(5)] for i in range(N)]

for i in range(N):
    word=list(map(int,input().split(' ')))
    arr[i]=word
    
Result=[]

for i in range(N):
    
    CNT=0
    temp=[]
    
    for j in range(5): 
        for k in range(N): 
            if (i!=k) and (arr[i][j]==arr[k][j]):
                temp.append(k)
                
    temp=list(set(temp))
    Result.append(len(temp))
                
print(Result.index(max(Result))+1)