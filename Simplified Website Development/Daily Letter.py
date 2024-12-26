from datetime import datetime

c = datetime.now()

current_time = c.strftime('%H:%M:%S')

print('Current Time is:', current_time)