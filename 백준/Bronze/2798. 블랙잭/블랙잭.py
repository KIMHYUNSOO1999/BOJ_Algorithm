N,M=map(int, input().split())
numbers=list(map(int, input().split()))

result=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            result_temp=numbers[i]+numbers[j]+numbers[k]
            if result_temp <= M and result < result_temp:
                result=result_temp
                
print(result)