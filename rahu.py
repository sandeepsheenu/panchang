# import ephem
# from datetime import datetime, timedelta

# def calculate_rahukala_yamagantha(date, latitude, longitude):
#     # Observer
#     obs = ephem.Observer()
#     obs.date = date
#     obs.lat = str(latitude)
#     obs.long = str(longitude)

#     # Get sunrise and sunset times in UTC
#     sunrise_utc = obs.previous_rising(ephem.Sun())
#     sunset_utc = obs.next_setting(ephem.Sun())
#     print(sunset_utc)
    
#     # Calculate total duration between sunrise and sunset
#     total_duration = sunset_utc - sunrise_utc
#     print(total_duration)
    
#     # Calculate duration for each part
#     interval_duration = total_duration / 8
    
#     # Initialize list to store start and end values of each part
#     parts = []
    
#     # Calculate start and end values for each part
#     for i in range(8):
#         start_time = sunrise_utc + i * interval_duration
#         end_time = start_time + interval_duration
#         parts.append((start_time, end_time))
    
#     return parts

# # Input date, latitude, and longitude
# date = ephem.now()
# latitude_input = 12.97
# longitude_input = 77.59

# # Calculate and print the start and end values of each part
# parts = calculate_rahukala_yamagantha(date, latitude_input, longitude_input)
# for i, (start_time, end_time) in enumerate(parts, start=1):
#     print(f"Part {i}: Start: {start_time}, End: {end_time}")


# import ephem
# from datetime import datetime, timedelta

# # Function to calculate sunrise and sunset times
# def calculate_sunrise_sunset(date):
#     obs = ephem.Observer()
#     obs.lat = '12.9716'  # Latitude of the location (Assuming Bangalore, India)
#     obs.lon = '77.5946'  # Longitude of the location (Assuming Bangalore, India)
#     obs.date = date

#     sunrise = obs.next_rising(ephem.Sun()).datetime().replace(tzinfo=None)
#     sunset = obs.next_setting(ephem.Sun()).datetime().replace(tzinfo=None)

#     return sunrise, sunset

# # Function to divide the day into 8 parts
# def divide_day(sunrise, sunset):
#     day_length = sunset - sunrise
#     part_length = day_length / 8
#     part_timings = [(sunrise + part_length * i, sunrise + part_length * (i + 1)) for i in range(8)]
#     return part_timings

# # Function to find the day of the given date
# def find_day_of_date(date):
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     day_index = date.weekday()
#     return days[day_index]

# # Main function
# def main():
#     date_input = input("Enter date (YYYY-MM-DD): ")
#     year, month, day = map(int, date_input.split("-"))
#     date = datetime(year, month, day)

#     sunrise, sunset = calculate_sunrise_sunset(date)
#     part_timings = divide_day(sunrise, sunset)
#     day_of_date = find_day_of_date(date)

#     print("Sunrise:", sunrise.time())
#     print("Sunset:", sunset.time())
#     print("Dividing day into 8 parts:")
#     for i, part in enumerate(part_timings):
#         print("Part {}: {} - {}".format(i + 1, part[0].time(), part[1].time()))

#     if day_of_date == "Monday":
#         print("Rahukalam timings (2nd part): {} - {}".format(part_timings[1][0].time(), part_timings[1][1].time()))

# if __name__ == "__main__":
#     main()
import ephem
from datetime import datetime, timedelta
import pytz

# Function to calculate sunrise and sunset times
def calculate_sunrise_sunset(date):
    obs = ephem.Observer()
    obs.lat = '12.9716'  # Latitude of the location (Assuming Bangalore, India)
    obs.lon = '77.5946'  # Longitude of the location (Assuming Bangalore, India)
    obs.date = date

    sunrise = obs.next_rising(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)
    sunset = obs.next_setting(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)

    return sunrise, sunset

# Function to divide the day into 8 parts
def divide_day(sunrise, sunset):
    day_length = sunset - sunrise
    part_length = day_length / 8
    part_timings = [(sunrise + part_length * i, sunrise + part_length * (i + 1)) for i in range(8)]
    #print(part_timings)
    return part_timings

# Function to find the day of the given date
def find_day_of_date(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date.weekday()
    return days[day_index]

# Main function
def main():
    date_input = input("Enter date (YYYY-MM-DD): ")
    year, month, day = map(int, date_input.split("-"))
    date = datetime(year, month, day)

    sunrise, sunset = calculate_sunrise_sunset(date)
    ist = pytz.timezone('Asia/Kolkata')
    sunrise = sunrise.astimezone(ist)
    sunset = sunset.astimezone(ist)

    part_timings = divide_day(sunrise, sunset)
    part_timings = [(start.astimezone(ist), end.astimezone(ist)) for start, end in part_timings]
    day_of_date = find_day_of_date(date)

    print("Sunrise (IST):", sunrise.strftime('%H:%M:%S'))
    print("Sunset (IST):", sunset.strftime('%H:%M:%S'))
    print("Dividing day into 8 parts:")
    for i, part in enumerate(part_timings):
        print("Part {}: {} - {}".format(i + 1, part[0].strftime('%H:%M:%S'), part[1].strftime('%H:%M:%S')))
        # values of parts  should be mins (-1) to get the exact timings due to zero index

    if day_of_date == "Monday":
        print("Rahukalam timings (2nd part): {} - {}".format(part_timings[1][0].strftime('%H:%M:%S'), part_timings[1][1].strftime('%H:%M:%S')))
        print("yamagandam  timings (4nd part): {} - {}".format(part_timings[3][0].strftime('%H:%M:%S'), part_timings[3][1].strftime('%H:%M:%S')))
        print(" Gulika timings (5nd part): {} - {}".format(part_timings[5][0].strftime('%H:%M:%S'), part_timings[5][1].strftime('%H:%M:%S')))
    if day_of_date == "Tuesday":
        print("Rahukalam timings (7nd part): {} - {}".format(part_timings[6][0].strftime('%H:%M:%S'), part_timings[6][1].strftime('%H:%M:%S')))
        print("yamagandam  timings (3nd part): {} - {}".format(part_timings[2][0].strftime('%H:%M:%S'), part_timings[2][1].strftime('%H:%M:%S')))
        print(" Gulika timings (4nd part): {} - {}".format(part_timings[4][0].strftime('%H:%M:%S'), part_timings[4][1].strftime('%H:%M:%S')))    
    if day_of_date == "Wednesday":
        print("Rahukalam timings (4nd part): {} - {}".format(part_timings[4][0].strftime('%H:%M:%S'), part_timings[4][1].strftime('%H:%M:%S')))
        print("yamagandam  timings (3nd part): {} - {}".format(part_timings[1][0].strftime('%H:%M:%S'), part_timings[1][1].strftime('%H:%M:%S')))
        print(" Gulika timings (4nd part): {} - {}".format(part_timings[3][0].strftime('%H:%M:%S'), part_timings[3][1].strftime('%H:%M:%S'))) 
    if day_of_date == "Thursday":
        print("Rahukalam timings (5nd part): {} - {}".format(part_timings[5][0].strftime('%H:%M:%S'), part_timings[5][1].strftime('%H:%M:%S')))
        print("yamagandam  timings (1nd part): {} - {}".format(part_timings[0][0].strftime('%H:%M:%S'), part_timings[0][1].strftime('%H:%M:%S')))
        print(" Gulika timings (4nd part): {} - {}".format(part_timings[2][0].strftime('%H:%M:%S'), part_timings[2][1].strftime('%H:%M:%S')))
    if day_of_date == "Friday":
        print("Rahukalam timings (5nd part): {} - {}".format(part_timings[3][0].strftime('%H:%M:%S'), part_timings[3][1].strftime('%H:%M:%S')))
        print("yamagandam  timings (1nd part): {} - {}".format(part_timings[6][0].strftime('%H:%M:%S'), part_timings[6][1].strftime('%H:%M:%S')))
        print(" Gulika timings (4nd part): {} - {}".format(part_timings[1][0].strftime('%H:%M:%S'), part_timings[1][1].strftime('%H:%M:%S')))      
    if day_of_date == "Saturday":
       
        print("Rahukalam timings (2nd part): {} - {}".format(part_timings[6][0].strftime('%H:%M:%S'), part_timings[2][1].strftime('%H:%M:%S')))
        print("yamagandam  timings (1nd part): {} - {}".format(part_timings[5][0].strftime('%H:%M:%S'), part_timings[5][1].strftime('%H:%M:%S')))
        print(" Gulika timings (4nd part): {} - {}".format(part_timings[0][0].strftime('%H:%M:%S'), part_timings[0][1].strftime('%H:%M:%S')))            
    
    if day_of_date == "Sunday":
        print("Rahukalam timings (2nd part): {} - {}".format(part_timings[7][0].strftime('%H:%M:%S'), part_timings[7][1].strftime('%H:%M:%S')))
        print("yamagandam  timings (1nd part): {} - {}".format(part_timings[4][0].strftime('%H:%M:%S'), part_timings[4][1].strftime('%H:%M:%S')))
        print(" Gulika timings (4nd part): {} - {}".format(part_timings[6][0].strftime('%H:%M:%S'), part_timings[6][1].strftime('%H:%M:%S'))) 
               

if __name__ == "__main__":
    main()
