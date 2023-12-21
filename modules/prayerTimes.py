import datetime, requests, time

from tools.getCoordinates import driver as get_coordinates
from tools.say import driver as say

API_CALL_LIMIT = 1e3

def get_url(query_time):
	year = query_time.year
	month = query_time.month
	day = query_time.day
	location = get_coordinates()
	latitude = location["latitude"]
	longitude = location["longitude"]
	url = f"http://api.aladhan.com/v1/calendar/{year}/{month}?latitude={latitude}&longitude={longitude}"
	return url

def filter_timings(now, query_time, timings):
	filtered_timings = []
	prayer_list = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]

	for prayer in prayer_list:
		hour = int(timings[prayer][:2])
		minute = int(timings[prayer][3:6])
		prayer_time = datetime.datetime(query_time.year, query_time.month, query_time.day, hour, minute, 0)
		
		if prayer_time > now:
			prayer_time_str = prayer_time.strftime("%I:%M %p")
			filtered_timings.append([prayer, prayer_time_str, (prayer_time - now).seconds])

	return filtered_timings		

def get_prayer_times(now, query_time, trial_number):
	url = get_url(query_time)
	try:
		response = requests.get(url)
		day = query_time.day
		timings = response.json()["data"][day - 1]["timings"]
		return filter_timings(now, query_time, timings)
	except:
		if trial_number < API_CALL_LIMIT:
			get_prayer_times(now, query_time, trial_number + 1)

def combine_prayers(list1, list2):
	combined_list = list1

	for item in list2:
		if len(combined_list) == 6:
			break

		combined_list.append(item)

	return combined_list

def driver():
	now = datetime.datetime.now()
	prayer_times_today = get_prayer_times(now, now, 1)
	prayer_times_tomorrow = get_prayer_times(now, now + datetime.timedelta(hours = 24), 1)

	if prayer_times_today == None or prayer_times_tomorrow == None:
		say("Couldn't get prayer times")
		return

	prayer_times = combine_prayers(prayer_times_today, prayer_times_tomorrow)
	next_prayer = prayer_times[0]
	hours_left = prayer_times[0][2] // (60 * 60)
	minutes_left = prayer_times[0][2] // 60 % 60

	say(f"{hours_left} hours and {minutes_left} minutes till {next_prayer[0]}")
	print(prayer_times)
	
	return prayer_times