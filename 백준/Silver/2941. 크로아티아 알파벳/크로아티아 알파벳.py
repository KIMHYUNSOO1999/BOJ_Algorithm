N=input()

search = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for row in search :
    N = N.replace(row, 'x')
    
print(len(N))