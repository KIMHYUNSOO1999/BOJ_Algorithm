import sys
input = sys.stdin.readline

N,M=map(int,input().rstrip().split(' '))

password={}

for i in range(N):
    A,B=map(str,input().rstrip().split(' '))
    password[A]=B
    
for i in range(M):
    A=input().rstrip()
    print(password[A])