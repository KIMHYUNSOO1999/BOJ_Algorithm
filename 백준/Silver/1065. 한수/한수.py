import sys
input=sys.stdin.readline

N = int(input())

result = 0

for i in range(1, N+1):
    number_list = list(map(int, str(i)))
    if i < 100:
        result += 1  
    elif number_list[0]-number_list[1] == number_list[1]-number_list[2]:
        result += 1  
        
print(result)