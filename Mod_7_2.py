from datetime import datetime, timedelta
d = datetime.today() - timedelta(seconds=60) + timedelta(hours=2)
d.strftime('%H:%M %p')
print(d) 