import sys
input = sys.stdin.readline

cnt1, cnt2 = map(int, input().split())

dict = {}
dict2 = {}
for i in range(cnt1):
    
    tmp=input().strip()
    dict[tmp]=i+1
    dict2[i+1]=tmp

for _ in range(cnt2):
    
    tmp=input().strip()
    
    if tmp.isdigit()==True:
        print(dict2.get(int(tmp)))
    else:
        print(dict[tmp])