import sys
input = sys.stdin.readline

charArr = list(map(str,input().rstrip().split()))
alphaArr = ['U','C','P','C']
answer = 0

for chrs in charArr:
    for chr in chrs:
        if answer == 4: 
            break
        if alphaArr[answer] in chr:
            answer +=1

if answer == 4:
    print("I love UCPC")
else: 
    print("I hate UCPC")