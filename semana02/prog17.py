import datetime
import pytz

data = datetime.date(2020, 7, 24)
print(data)

tday = datetime.date.today()
print(tday)

print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)


# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2021, 7, 13)
till_bday = bday - tday
print(till_bday.days)
print(till_bday)
print(till_bday.total_seconds())


t = datetime.time(21, 29, 10, 100000)
print(t)
t = datetime.date(2021, 3, 18)
print(t)
t = datetime.datetime(2021, 3, 18, 21, 32, 10, 100000)
print(t)
print(t.date())
print(t.time())

#===========================================#

print(t + tdelta)

tdelta = datetime.timedelta(hours=12)
print(t + tdelta)

#===========================================#

dt_today = datetime.datetime.today()

print(dt_today)

#===========================================#

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_br = dt_utcnow.astimezone(pytz.timezone('Brazil/East'))
print(dt_br)

#for tz in pytz.all_timezones:
	#print(tz)

#===========================================#

dt_br = datetime.datetime.now()
dt_east = dt_br.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

#===========================================#

dt_br = datetime.datetime.now(tz=pytz.timezone('Brazil/East'))
print(dt_br.strftime('%B %d, %Y'))

dt_str = 'March 18, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt.date())