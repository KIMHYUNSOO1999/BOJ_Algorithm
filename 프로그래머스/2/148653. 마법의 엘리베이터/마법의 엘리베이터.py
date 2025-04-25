def solution(storey):
    
    answer = 0
    flag = False
    digits = list(str(storey))[::-1]

    for idx in range(len(digits)):
        
        i = digits[idx]
        if flag:
            tmp = int(i) + 1
        else:
            tmp = int(i)

        if tmp > 5:
            flag = True
            answer += 10 - tmp
        elif tmp == 5:
            if idx + 1 < len(digits) and int(digits[idx + 1]) >= 5:
                flag = True
            else:
                flag = False
            answer += 5
        else:
            flag = False
            answer += tmp

    if flag:
        answer += 1

    return answer
