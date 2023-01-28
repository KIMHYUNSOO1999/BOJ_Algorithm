N = int(input())
arr= [i+1 for i in range(N)]

i=0
result=' '

while True:
    if len(arr)==1:
        result+=f'{arr[0]}'
        break
        
    result+=f'{arr[0]} '
    del arr[0]
    
    arr.append(arr[0])
    del arr[0]
    i+=1
    
print(result.strip())