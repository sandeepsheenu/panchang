import ephem
import pytz
from datetime import datetime

def calculate_vikram_samvat(observer):
    # Create a Sun object
    sun = ephem.Sun()

    # Set the observer's location
    observer.date = ephem.now()

    # Compute the Sun's position
    sun.compute(observer)

    # Determine the date of the Hindu New Year (Chaitra Shukla Pratipada)
    new_year_date = ephem.localtime(ephem.previous_new_moon(observer.date))

    # Calculate the Vikram Samvat year
    vikram_samvat_year = new_year_date.year + 57

    return vikram_samvat_year

# Example: Print the current Vikram Samvat for Bangalore in IST
def get_vikram_samvat_for_bangalore():
    # Bangalore's coordinates
    bangalore_location = {'latitude': 12.9716, 'longitude': 77.5946}

    # Create an observer
    observer = ephem.Observer()
    observer.lat = str(bangalore_location['latitude'])
    observer.lon = str(bangalore_location['longitude'])

    # Calculate Vikram Samvat
    current_vikram_samvat = calculate_vikram_samvat(observer)

    # Convert to IST
    utc_time = datetime.utcnow()
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = pytz.utc.localize(utc_time).astimezone(ist_timezone)

    print(f'Current Vikram Samvat in Bangalore (IST): {current_vikram_samvat} as of {ist_time}')

# Run the example
get_vikram_samvat_for_bangalore()


import calendar

def get_days_in_month(year, month):
    # Use monthrange() function from calendar to get the number of days in a month
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month

# Example usage:
year = 2024

month = 2  # February

days_in_february_2022 = get_days_in_month(year, month)
print(f"Number of days in {calendar.month_name[month]}, {year}: {days_in_february_2022}")

