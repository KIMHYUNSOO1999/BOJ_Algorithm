N = input()

comp = len(N) - 1
answer = 0

for i in range(comp):
    answer += 9 * (10 ** i) * (i + 1)
    i += 1
    
answer += ((int(N) - (10 ** comp)) + 1) * (comp + 1)

print(answer)