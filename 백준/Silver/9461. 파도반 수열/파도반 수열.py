N=int(input())

arr= [0]*100

arr[0]=1
arr[1]=1
arr[2]=1

for i in range(3,100):
    arr[i]=arr[i-2]+arr[i-3]
    
for i in range(N):
    print(arr[int(input())-1])