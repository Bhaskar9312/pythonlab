import pandas as pd
from datetime import datetime

dt_a = pd.to_datetime('2012-01-15')
print("Date time object for Jan 15 2012:", dt_a)

dt_b = pd.to_datetime('2012-01-15 21:20:00')
print("Specific date and time of 9:20 pm:", dt_b)

dt_c = pd.Timestamp.now()
print("Local date and time:", dt_c)

dt_d = pd.to_datetime('2023-04-08').date()
print("A date without time:", dt_d)

dt_e = pd.Timestamp.today().date()
print("Current date:", dt_e)

dt_f = dt_c.time()
print("Time from a date time:", dt_f)

dt_g = datetime.now().time()
print("Current local time:", dt_g)
