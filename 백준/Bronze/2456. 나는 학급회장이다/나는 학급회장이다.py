import sys
input = sys.stdin.readline

arr = {
    1: [0, 0, 0], 
    2: [0, 0, 0],
    3: [0, 0, 0]
}

N = int(input().rstrip())
for _ in range(N):
    a, b, c = map(int, input().split())
    
    votes = [a, b, c]
    for i in range(3):
        tmp = i+1
        score = votes[i]
        
        arr[tmp][0] += score  
        
        if score == 3:
            arr[tmp][1] += 1
        elif score == 2:
            arr[tmp][2] += 1

arr = sorted(arr.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True)

first = arr[0]
second = arr[1]

if first[1] == second[1]:
    print(0, first[1][0])
else:
    print(first[0], first[1][0])