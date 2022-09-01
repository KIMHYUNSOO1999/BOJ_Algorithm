str_list=[]
N=int(input())
    
for i in range(0,N):
    i=input()
    str_list.append(i)

str_list=list(set(str_list))

str_list.sort()
str_list.sort(key=len)

for rows in str_list:
    print(rows)