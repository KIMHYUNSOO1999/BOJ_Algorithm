N=int(input())

for i in range(0,N):
    word=input()
    for j in range(len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            N-=1
            break
print(N)