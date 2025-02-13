import sys
input = sys.stdin.readline

for i in range(3):
    tmp=input().strip()
    
    if tmp.isdigit()==True:
        a, b = i, int(tmp)

tmp2 = b+(3-a)

if tmp2%3==0 and tmp2%5==0:
    print('FizzBuzz')
elif tmp2%3==0:
    print('Fizz')
elif tmp2%5==0:
    print('Buzz')
else:
    print(tmp2)