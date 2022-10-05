answer=[]

while(True):
    N=input()
    if N=='0': break
        
    if N == N[::-1]:
        answer.append('yes')
    else:
        answer.append('no')

for row in answer:
    print(row)