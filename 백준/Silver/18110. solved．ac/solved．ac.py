import sys
input = sys.stdin.readline

def round(value):
    return int(value)+1 if value - int(value) >= 0.5 else int(value)

cnt = int(input())

if cnt>0: 
    arr = []
    for i in range(cnt):
        arr.append(int(input()))
        
    std= round(len(arr)*0.15)
    
    arr.sort()
    arr=arr[std:len(arr)-std]
    
    print(round(sum(arr)/len(arr)))
else:
    print(0)