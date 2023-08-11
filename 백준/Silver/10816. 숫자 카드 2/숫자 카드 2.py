import sys
input=sys.stdin.readline

standard_num=int(input())
standard_list=list(map(int,input().split(' ')))

tmp_num=int(input())
tmp_list=list(map(int,input().split(' ')))

result={}

for i in standard_list:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
        
for i in tmp_list:
    if i in result:
        print(result[i], end=' ') 
    else:
        print(0, end=' ')