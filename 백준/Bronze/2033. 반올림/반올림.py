import sys
input = sys.stdin.readline

s = list(map(int,input().rstrip()))[::-1]

for i in range(len(s)):
    if i != len(s)-1 and s[i]>=5:
       s[i+1]+=1 
       s[i]=0
    elif i != len(s)-1:
       s[i]=0

for i in s[::-1]:
    print(i, end='')