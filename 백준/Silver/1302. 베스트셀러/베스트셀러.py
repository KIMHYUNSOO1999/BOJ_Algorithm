import sys
input=sys.stdin.readline

arr={}
N=int(input())

for _ in range(N):
    word=input().rstrip()
    
    if word in arr:
        arr[word]+=1
    else:
        arr[word]=1
        
CNT=0

arr=dict(sorted(arr.items()))
for word in arr:
    if(arr[word]>CNT):
        CNT=arr[word]
        Result=word
        
print(Result)