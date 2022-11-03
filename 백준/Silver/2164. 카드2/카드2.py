N = int(input())
square = 2

while True:
    
    square *= 2
    
    if (N == 1 or N == 2):
        print(N)
        break

    if (square >= N):
        print((N - (square // 2)) * 2)
        break