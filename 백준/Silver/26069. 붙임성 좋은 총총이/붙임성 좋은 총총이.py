import sys
input = sys.stdin.readline

n = int(input().rstrip())

chk = set()
for _ in range(n):
    
    a, b = input().strip().split()

    if a == "ChongChong" or b == "ChongChong":
        chk.add(a)
        chk.add(b)

    if a in chk or b in chk:
        chk.add(a)
        chk.add(b)
        
print(len(chk))