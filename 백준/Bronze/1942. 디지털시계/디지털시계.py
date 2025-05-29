import sys
input = sys.stdin.readline

while True:
    try:
        start, end = list(map(str, input().strip().split()))
            
        result = 0
        
        while True:
            
            hh, mm, ss = map(str, start.split(':'))
            
            time = int(hh+mm+ss)
            
            if time%3==0:
                result +=1

            if start == end:
                break
            
            ss = int(ss)+1
            mm = int(mm)
            hh = int(hh)
            
            if ss >=60:
                ss = 0
                mm += 1
            
            if mm >= 60:
                mm = 0
                hh += 1
            
            if hh >= 24:
                hh = 0
                mm = 0
                ss = 0
            
            start = f'{hh:02}:{mm:02}:{ss:02}'
            
        print(result)
        
    except:
        break