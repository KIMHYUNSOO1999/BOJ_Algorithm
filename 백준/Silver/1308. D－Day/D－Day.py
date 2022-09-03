from datetime import datetime

today=list(map(int,input().split()))
target=list(map(int,input().split()))

today_date=datetime(year=today[0],month=today[1],day=today[2])
target_date=datetime(year=target[0],month=target[1],day=target[2])

over_date=datetime(year=today[0]+1000,month=today[1],day=today[2])

if target_date - today_date >= over_date-today_date:
    print("gg")
else:
    result=target_date-today_date
    print(f"D-{result.days}")