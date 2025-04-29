def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def notDiv(array, x):
    for n in array:
        if n % x == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0

    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for n in arrayA[1:]:
        gcdA = gcd(gcdA, n)
        
    for n in arrayB[1:]:
        gcdB = gcd(gcdB, n)
        
    if gcdB != 1 and notDiv(arrayA, gcdB):
        answer = max(answer, gcdB)
    
    if gcdA != 1 and notDiv(arrayB, gcdA):
        answer = max(answer, gcdA)
        
    return answer
