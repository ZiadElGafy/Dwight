import datetime

from modules.prayerTimes import combine_prayers
from modules.prayerTimes import get_prayer_times

from tools.say import driver as say

def driver():
	now = datetime.datetime.now()
	prayer_times_today = get_prayer_times(now, now, 1)
	prayer_times_tomorrow = get_prayer_times(now, now + datetime.timedelta(hours = 24), 1)

	if prayer_times_today == None or prayer_times_tomorrow == None:
		say("Couldn't get prayer times.")
		return

	prayer_times = combine_prayers(prayer_times_today, prayer_times_tomorrow)
	
	next_prayer = prayer_times[0]
	hours_left = prayer_times[0][2] // (60 * 60)
	minutes_left = prayer_times[0][2] // 60 % 60

	say(f"{hours_left} hours and {minutes_left} minutes till {next_prayer[0]}")
	print(prayer_times)