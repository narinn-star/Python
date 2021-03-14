#module _ strftime

import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))