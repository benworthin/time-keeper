import os
import csv
# from datetime import date
# from datetime import time
from datetime import datetime

today = datetime.today()
now = today.strftime('%m-%d-%y %I:%M %p')

print(now)