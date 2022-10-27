import sys
input=sys.stdin.readline 

num_list=[]
max_num=0
n=0

for _ in range(9):
    num_list.append(int(input()))
    
for row in num_list:
    n+=1
    if row>=max_num:
        max_num=row
        result_b=row
        result_a=n
    
print(result_b)
print(result_a)