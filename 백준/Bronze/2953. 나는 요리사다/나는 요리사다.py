arr=[]
arr_sum=[]

for i in range(5):
    arr.append(list(map(int,input().split(' '))))
    arr_sum.append(sum(arr[i]))
    
print(arr_sum.index(max(arr_sum))+1,max(arr_sum))