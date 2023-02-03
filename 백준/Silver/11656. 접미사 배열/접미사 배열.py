import sys
input=sys.stdin.readline

word = input().rstrip()

arr=[]

for i in range(len(word)):
    arr.append(word[i:len(word)])

for result in sorted(arr):
    print(result)