from datetime import datetime

mytime = datetime.strptime(input().strip(),'%I:%M:%S%p')
print(mytime.strftime("%H:%M:%S"))