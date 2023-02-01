import sys
input=sys.stdin.readline

CNT=0

for _ in range(int(input())):
    arr=[]
    word=input().rstrip()

    for i in range(len(word)):
        if arr and word[i] == arr[-1]:
            arr.pop()
        else:
            arr.append(word[i])
            
    if not arr:
        CNT+=1
        
print(CNT)