# import pytz
# import datetime
#
# country = "Europe/Moscow"
#
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The time in {} is {}". format(country, local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)
# print("=" * 40)
#
# for x in sorted(pytz.country_names):
#     print(x + ":" + pytz.country_names[x])
#
# print("=" * 40)
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))


# import datetime
#
# import pytz
#
# local_time = datetime.datetime.now()
# utc_time = datetime.datetime.utcnow()
# print("Naive local time {}".format(local_time))
# print("Naive UTC {}".format(utc_time))
#
# aware_local_time = pytz.utc.localize(utc_time).astimezone()
# aware_utc_time = pytz.utc.localize(utc_time)
# print("Aware local time {} time zone {}".format(aware_local_time, aware_local_time.tzinfo))
# print("Aware UTC time {} time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))
#
# gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
# print(gap_time)
# print(gap_time.timestamp())
#
# s = 1445733000
# t = s + (60*60)
#
# gb = pytz.timezone('GB')
# dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
# dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)
#
# print("{} seconds since the epoch is {}".format(s, dt1))
# print("{} seconds since the epoch is {}".format(t, dt2))

import pytz
import datetime

country = input("Please select a time zone from the following list: Africa/Dakar, America/Belize, "
                "America/Buenos_Aires, America/Vancouver, Asia/Bangkok, Egypt, Europe/Rome, Jamaica, Portugal:   ")

while country:
    if country == "0":
        print("exiting from program")
        break
    else:
        if country in pytz.all_timezones:
            tz_to_display = pytz.timezone(country)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("The time in {} is {} {}". format(country, local_time.strftime('%A %x %X %z'), local_time.tzname()))
            utc_time = datetime.datetime.utcnow()
            print("UTC is {}".format(utc_time.strftime('%A %x %X %z')))
            local_time = datetime.datetime.now()
            print("The local time is {}". format(local_time.strftime('%A %x %X %z')))
            country = input("Please enter time zone: ")
        else:
            print("Error - not in all_times zones")
            country = input("Please enter another time zone: ")
