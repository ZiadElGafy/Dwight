import datetime

from tools.say import driver as say

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemner", "December"]

day_number = [
    "first", "second", "third", "fourth", "fifth",
    "sixth", "seventh", "eighth", "ninth", "tenth",
    "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth",
    "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth",
    "twenty-first", "twenty-second", "twenty-third", "twenty-fourth", "twenty-fifth",
    "twenty-sixth", "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth",
    "thirty-first"
]

def get_date():
    date = datetime.datetime.now().date()
    say(f"Today is the {day_number[date.day - 1]} of {month_names[date.month - 1]} {date.year}")

def get_time():
    time = datetime.datetime.now()
    time_str = time.strftime("%I:%M %p")
    say(f"It is now {time_str}")