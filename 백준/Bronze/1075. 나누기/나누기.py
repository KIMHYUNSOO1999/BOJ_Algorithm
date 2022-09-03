N = input()
F = int(input())

divide = int(N[:-2] + '00')

while True:
    if  divide % F == 0:
        break
    divide += 1

print(str(divide)[-2:])