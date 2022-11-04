N_word=input()
result=0 

for row in N_word:
    if ord(row) < 80:
        result+=(ord(row)-65)//3
        result+=3
    elif ord(row) in(80,81,82,83):
        result+=8
    elif ord(row) in(84,85,86):
        result+=9
    else:
        result+=10
        
print(result)