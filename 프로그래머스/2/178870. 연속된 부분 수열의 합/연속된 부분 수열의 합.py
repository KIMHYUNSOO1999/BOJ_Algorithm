def solution(sequence, k):
    
    answer = []
    start, end = 0, 0
    min_len = 1000001  
    part_sum = sequence[0] 

    while start <= end < len(sequence):
            
        if part_sum == k:
            if end - start + 1 < min_len:
                answer = [start, end]
                min_len = end - start + 1
            part_sum -= sequence[start]
            start += 1

        elif part_sum < k:
            end += 1
            if end < len(sequence):
                part_sum += sequence[end]

        elif part_sum > k:
            part_sum -= sequence[start]
            start += 1

    return answer