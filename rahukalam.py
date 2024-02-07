# def day_of_week(day, month, year):
#     # Months' codes from Zeller's Congruence
#     month_codes = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
#     # Days of the week
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
#     if month < 3:
#         year -= 1
#     # Calculate the day of the week
#     day_of_week = (year + year // 4 - year // 100 + year // 400 + month_codes[month - 1] + day) % 7
    
#     return days[day_of_week]

# # Example usage:
# day = 9
# month = 2
# year = 2024

# print(day_of_week(day, month, year))


# from datetime import datetime, timedelta

# # Function to calculate the timings for each part between sunrise and sunset
# def calculate_parts(sunrise, sunset):
#     # Total duration between sunrise and sunset
#     total_duration = sunset - sunrise

#     # Duration of each part
#     part_duration = total_duration / 8

#     # Initialize variables to store part timings
#     part1_start = sunrise
#     part2_start = part1_start + part_duration
#     part3_start = part2_start + part_duration
#     part4_start = part3_start + part_duration
#     part5_start = part4_start + part_duration
#     part6_start = part5_start + part_duration
#     part7_start = part6_start + part_duration
#     part8_start = part7_start + part_duration

#     part1_end = part2_start
#     part2_end = part3_start
#     part3_end = part4_start
#     part4_end = part5_start
#     part5_end = part6_start
#     part6_end = part7_start
#     part7_end = part8_start
#     part8_end = sunset

#     return (part1_start, part1_end), (part2_start, part2_end), (part3_start, part3_end), \
#            (part4_start, part4_end), (part5_start, part5_end), (part6_start, part6_end), \
#            (part7_start, part7_end), (part8_start, part8_end)

# # Example usage
# if __name__ == "__main__":
#     # Input sunrise and sunset times (replace with actual times)
#     sunrise = datetime.strptime("06:45", "%H:%M")  # Example: 6:30 AM
#     sunset = datetime.strptime("18:22", "%H:%M")   # Example: 6:30 PM

#     # Calculate part timings
#     part1, part2, part3, part4, part5, part6, part7, part8 = calculate_parts(sunrise, sunset)

#     # Print part timings
#     print("Part 1 ->", part1[0].strftime('%H:%M'), "to", part1[1].strftime('%H:%M'))
#     print("Part 2 ->", part2[0].strftime('%H:%M'), "to", part2[1].strftime('%H:%M'))
#     print("Part 3 ->", part3[0].strftime('%H:%M'), "to", part3[1].strftime('%H:%M'))
#     print("Part 4 ->", part4[0].strftime('%H:%M'), "to", part4[1].strftime('%H:%M'))
#     print("Part 5 ->", part5[0].strftime('%H:%M'), "to", part5[1].strftime('%H:%M'))
#     print("Part 6 ->", part6[0].strftime('%H:%M'), "to", part6[1].strftime('%H:%M'))
#     print("Part 7 ->", part7[0].strftime('%H:%M'), "to", part7[1].strftime('%H:%M'))
#     print("Part 8 ->", part8[0].strftime('%H:%M'), "to", part8[1].strftime('%H:%M'))


# def ra_ya( days,)
import ephem
from datetime import datetime, timedelta

def get_sunrise_sunset(date):
    obs = ephem.Observer()
    obs.lat = '12.9739'  # Latitude for New Delhi, India
    obs.lon = '77.7790'  # Longitude for New Delhi, India
    obs.date = date
    sun = ephem.Sun(obs)
    sunrise_utc = obs.previous_rising(sun).datetime().strftime('%H:%M:%S')
    sunset_utc = obs.next_setting(sun).datetime().strftime('%H:%M:%S')
    
    # Convert UTC timings to IST
    sunrise_ist = (datetime.strptime(sunrise_utc, "%H:%M:%S") + timedelta(hours=5, minutes=30)).strftime('%H:%M:%S')
    sunset_ist = (datetime.strptime(sunset_utc, "%H:%M:%S") + timedelta(hours=5, minutes=30)).strftime('%H:%M:%S')
    
    return sunrise_ist, sunset_ist

def get_day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = datetime.strptime(date, "%Y-%m-%d").weekday()
    return days[day_of_week]

def divide_timings(sunrise, sunset):
    sunrise_time = datetime.strptime(sunrise, "%H:%M:%S")
    sunset_time = datetime.strptime(sunset, "%H:%M:%S")
    time_diff = sunset_time - sunrise_time
    interval = time_diff.total_seconds() / 8
    timings = [sunrise_time.strftime('%H:%M:%S')]
    current_time = sunrise_time
    for _ in range(7):
        current_time += timedelta(seconds=interval)
        timings.append(current_time.strftime('%H:%M:%S'))
    return timings



date = input("Enter the date (YYYY-MM-DD): ")
sunrise, sunset = get_sunrise_sunset(date)
day_of_week = get_day_of_week(date)
timings = divide_timings(sunrise, sunset)

print("Sunrise (IST):", sunrise)
print("Sunset (IST):", sunset)
print("Day of the week:", day_of_week)
print("Divided timings:")
for i, timing in enumerate(timings, 1):
    print(f"Part {i}: {timing}")
