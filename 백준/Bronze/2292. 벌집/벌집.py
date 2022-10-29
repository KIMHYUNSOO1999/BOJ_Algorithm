import sys
input=sys.stdin.readline 

N=int(input())

honeycomb = 1  
result = 1

while N > honeycomb :
    honeycomb += 6 * result  
    result += 1 
    
print(result)