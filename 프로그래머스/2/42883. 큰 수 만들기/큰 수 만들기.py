def solution(number, k):

    s = []
    for num in number:
        while k > 0 and s and s[-1] < num:
            s.pop()
            k -= 1
            
        s.append(num)
    
    if k != 0:
        s = s[:-k]
    
    return ''.join(s)