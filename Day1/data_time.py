import datetime

current_date_time = datetime.datetime.utcnow()
print(current_date_time)

"""
    asian time
"""
current_date_time1 = datetime.datetime.now()
print(current_date_time1)

from dateutil.relativedelta import relativedelta

"""
    relativedelta
"""
current_date_time1 += relativedelta(days=30)

print(current_date_time)

current_date_time -= relativedelta(years=1)
print(current_date_time)

""" 
    timedelta
"""

from datetime import timedelta

current_date_time -= timedelta(years=20)
print(current_date_time)
current_date_time = datetime.datetime.utcnow()
print(current_date_time)

"""
    asian time
"""


from dateutil.relativedelta import relativedelta

"""
    relativedelta
"""


""" 
    timedelta
"""


