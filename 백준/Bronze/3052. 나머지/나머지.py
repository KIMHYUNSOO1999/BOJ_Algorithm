Remainder=[]
for _ in range(10):
    word=int(input())
    Remainder.append(word%42)
    
Remainder=list(set(Remainder))
print(len(Remainder))