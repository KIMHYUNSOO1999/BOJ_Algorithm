import sys
input = sys.stdin.readline

dict = {
    'AA' : 'A',
    'AG' : 'C',
    'AC' : 'A',
    'AT' : 'G',
    'GA' : 'C',
    'GG' : 'G',
    'GC' : 'T',
    'GT' : 'A',
    'CA' : 'A',
    'CG' : 'T',
    'CC' : 'C',
    'CT' : 'G',
    'TA' : 'G',
    'TG' : 'A',
    'TC' : 'G',
    'TT' : 'T'
}

l = int(input())
arr=list(input().strip())

while len(arr)>1:
    a = arr.pop()
    b = arr.pop() 

    arr.append(dict[a+b])

print(*arr)
    