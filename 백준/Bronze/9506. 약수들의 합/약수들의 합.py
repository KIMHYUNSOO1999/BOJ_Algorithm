import sys
input = sys.stdin.readline

while True:

    n = int(input())

    if n == -1:
        break
    
    tmp = []
    for i in range(1,(n//2)+1):
        if n % i == 0:
            tmp.append(i)
    
    if n == sum(tmp):
        print(f"{n} = {' + '.join(map(str, tmp))}")
    else:
        print(f"{n} is NOT perfect.")