import sys
input=sys.stdin.readline

tmp,tmp2=map(str,input().rstrip().split(' '))

a=set(map(int,input().rstrip().split(' ')))
b=set(map(int,input().rstrip().split(' ')))

print(len(a-b)+len(b-a))