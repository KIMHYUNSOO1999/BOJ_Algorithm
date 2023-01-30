N=int(input())

CNT=1

for _ in range(N):
    
    arr=list(map(str,input().split(' ')))
    
    if len(arr)==1:
        print(f'Case #{CNT}: {arr[0]}')
    else:
        for i in range(len(arr)-1,-1,-1):
            if i== 0:
                print(arr[i])
            elif i==len(arr)-1:
                print(f'Case #{CNT}: {arr[i]}',end=' ')
            else:
                print(arr[i],end=' ')
                
    CNT+=1