import sys
input = sys.stdin.readline


N=int(input())
oil=list(map(int,input().rstrip().split(' ')))
price=list(map(int,input().rstrip().split(' ')))

min_price = oil[0] * price[0]
min_cost = oil[0]

for i in range(1,N-1):
    if min_cost > price[i]:
        min_cost = price[i]
        
    min_price += min_cost * oil[i]
    
print(min_price)