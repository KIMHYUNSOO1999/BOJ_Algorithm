def solution(phone_book):
    phone_book.sort()
    answer = True
    
    for i,j in zip(phone_book,phone_book[1:]):
        if j.startswith(i):
            answer=False
            break
        
    return answer