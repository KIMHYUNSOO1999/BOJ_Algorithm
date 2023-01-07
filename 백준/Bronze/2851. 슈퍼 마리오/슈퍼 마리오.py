number_list=[]
Result_list=[]
N_sum=0

for _ in range(10):
    N=int(input())
    number_list.append(N)

for num in number_list:
    if N_sum>100:
        break
    N_sum+=num
    Result_list.append(N_sum)
    
if abs(100-Result_list[-1])<=abs(100-Result_list[-2]):
    print(Result_list[-1])
else:
    print(Result_list[-2])
    
    
    