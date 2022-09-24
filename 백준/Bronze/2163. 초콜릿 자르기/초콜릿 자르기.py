N,M =map(int,input().split(" "))

sum=N*M

if sum==1:
    print("0")
else:
    print(sum-1)