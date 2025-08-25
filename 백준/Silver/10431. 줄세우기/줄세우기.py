import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    
    data = list(map(int, input().rstrip().split()))
    T, heights = data[0], data[1:]
    
    line = []
    moves = 0
    for h in heights:
        
        pos = len(line)
        for i in range(len(line)):
            
            if line[i] > h:
                pos = i
                break
                
        moves += len(line) - pos
        line.insert(pos, h)
        
    print(T, moves)