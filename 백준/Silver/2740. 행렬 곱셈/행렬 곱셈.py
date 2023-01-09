toggle=0

for _ in range(2):
    
    X,Y=map(int,(input().split(' ')))
    
    if toggle==0:
        A = [[0 for j in range(Y)] for i in range(X)]
    else:
        B = [[0 for j in range(Y)] for i in range(X)]
        
    for i in range(X):
        
        num_list=[]
        j=0
        
        num_list=list(map(int,(input().split(' '))))
            
        if toggle==0:
            for num in num_list:
                A[i][j]=num
                j+=1
        else:
            for num in num_list:
                B[i][j]=num
                j+=1
    toggle=1
    
Result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            Result[i][j] += (A[i][k] * B[k][j])
            
for i in Result:
    for j in i:
        print(j, end = ' ')
    print()