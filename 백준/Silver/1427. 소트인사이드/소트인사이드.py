N=input()
sort_N=[]

for i in range(len(N)):
    sort_N.append(N[i])

sort_N.sort(reverse=True)

for row in sort_N:
    print(row, end='')