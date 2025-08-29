def change_min(str_time):
    
    return int(str_time[0:2]) * 60 + int(str_time[3:])  

def solution(book_time):
    
    book_times = sorted([[change_min(i[0]), change_min(i[1]) + 10] for i in book_time])
    rooms = []
    
    for book_time in book_times:
        if not rooms:
            rooms.append(book_time)
            continue

        flag = False  
        for index, room in enumerate(rooms):
            if book_time[0] >= room[-1]:
                rooms[index] = room + book_time
                flag = True
                break
        
        if not flag:  
            rooms.append(book_time)

    return len(rooms)
