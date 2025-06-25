import sys
input = sys.stdin.readline

student = int(input())
switch = [0] + list(map(int,input().strip().split()))

n = int(input())
for _ in range(n):
    sex, w = map(int, input().strip().split())

    if sex == 1:
        for i in range(w, student+1, w):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    elif sex == 2:
        if switch[w] == 0:
            switch[w] = 1
        else:
            switch[w] = 0  

        for i in range(student//2):
            if w+i > student or w-i < 1:
                break

            if switch[w+i] == switch[w-i]:
                if switch[w+i] == 0:
                    switch[w+i] = 1
                else:
                    switch[w+i] = 0  
                if switch[w-i] == 0:
                    switch[w-i] = 1
                else:
                    switch[w-i] = 0  
            else:
                break
                
for i in range(1, student+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()
    
