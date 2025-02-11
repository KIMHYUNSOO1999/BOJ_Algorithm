import sys
input = sys.stdin.readline

# GCD
def GCD(n1,n2):

    while n2>0:
        n1, n2 = n2, n1%n2

    return n1

# LCM
def LCM(n1,n2):

    return n1 * n2 // GCD(n1, n2)
    
A, B = map(int,input().split())
print(GCD(A,B))
print(LCM(A,B))           

           
