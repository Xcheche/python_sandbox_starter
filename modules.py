from datetime import datetime

today_datetime = datetime.now()
today_date = today_datetime.date()
current_time = today_datetime.time()

print("Today's date:", today_date)
print("Current time:", current_time)
