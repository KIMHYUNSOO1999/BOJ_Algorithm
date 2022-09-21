N=int(input())
print_rs=[]
print_temp=""

for _ in range(N):
    R,S = map(str, input().split())
    for i in range(len(S)):
        for _ in range(int(R)):
             print_temp+=f'{S[i]}'
    print_rs.append(print_temp)
    print_temp=""
    
for row in print_rs:
    print(row)