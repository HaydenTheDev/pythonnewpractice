import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(local_time)
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware local time {}, time time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2020, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (60 + 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)

