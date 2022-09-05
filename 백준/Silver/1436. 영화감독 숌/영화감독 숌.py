N=int(input())

count=0
number=1

while True:
    if "666" in str(number):
        
        count=count+1

    if count==N:
        break

    number=number+1
    
print(number)