import requests
import datetime
import time

import os
from dotenv import load_dotenv
load_dotenv()

API_CALL_LIMIT = 1e3

def zero_padding(x):
	x = str(x)
	return x if len(x) == 2 else "0" + x

def get_url(query_time):
	COUNTRY = os.getenv("COUNTRY")
	CITY = os.getenv("CITY")
	year = query_time.year
	month = zero_padding(query_time.month)
	day = zero_padding(query_time.day)
	url = f"https://api.aladhan.com/v1/timingsByCity/{day}-{month}-{year}?city={CITY}&country={COUNTRY}"
	return url

def filter_timings(now, query_time, timings):
	filtered_timings = []
	prayer_list = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]

	for prayer in prayer_list:
		hour = int(timings[prayer][:2])
		minute = int(timings[prayer][3:])
		prayer_time = datetime.datetime(query_time.year, query_time.month, query_time.day, hour, minute, 0)
		if prayer_time > now:
			prayer_time_str = prayer_time.strftime("%I:%M %p")
			filtered_timings.append([prayer, prayer_time_str, (prayer_time - now).seconds])

	return filtered_timings		

def get_prayer_times(now, query_time, try_number):
	url = get_url(query_time)

	try:
		query_string = {
			"country":"Egypt",
			"city":"Cairo"
		}

		headers = {
			"X-RapidAPI-Key": os.getenv("X-RAPIDAPI-KEY"),
			"X-RapidAPI-Host": "aladhan.p.rapidapi.com"
		}

		response = requests.get(url, headers = headers, params = query_string)
		timings = response.json()["data"]["timings"]
		return filter_timings(now, query_time, timings)
	except:
		if try_number < API_CALL_LIMIT:
			get_prayer_times(now, query_time, try_number + 1)

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
		print("Couldn't get prayer times")
		return

	prayer_times = combine_prayers(prayer_times_today, prayer_times_tomorrow)
	next_prayer = prayer_times[0]
	hours_left = prayer_times[0][2] // (60 * 60)
	minutes_left = prayer_times[0][2] // 60 % 60

	print(f"{hours_left} hours and {minutes_left} minutes till {next_prayer[0]}")
	print(prayer_times)
	
	return prayer_times