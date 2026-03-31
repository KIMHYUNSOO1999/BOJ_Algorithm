import sys
input = sys.stdin.readline

geminis = list(map(int,input().rstrip().split()))
startRink = list(map(int,input().rstrip().split()))

scoreA = 0
scoreB = 0
lead = False

for i in range(9):
    scoreA += geminis[i]
    if scoreA > scoreB:
        lead = True
    scoreB += startRink[i]

if lead:
    print("Yes")
else:
    print("No")