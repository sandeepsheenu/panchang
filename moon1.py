import ephem

def calculate_moon_rise_set(observer, date):
    # Set the observer's location
    observer = ephem.Observer()
    observer.lat = '12.97'  # Latitude of a location
    observer.lon = '77.59'  # Longitude of a location
    # Set the date for which you want to calculate the moon rise and set times
    observer.date = date

    # Calculate the moon rise and set times
    moon_rise = observer.previous_rising(ephem.Moon())
    moon_set = observer.next_setting(ephem.Moon())

    return moon_rise, moon_set

# Example usage
observer = ephem.Observer()
date = ephem.now()  # Replace with the date for which you want to calculate the moon rise and set times
moon_rise, moon_set = calculate_moon_rise_set(observer, date)

print(f'Moon Rise: {moon_rise}')
print(f'Moon Set: {moon_set}')


import ephem
import pytz

def calculate_moon_rise_set(observer, date):
    # Set the observer's location
    observer.lat = '12.97'  # Latitude of a location
    observer.lon = '77.56'  # Longitude of a location
    # Convert date string to a datetime object
    observer.date = date

    # Calculate the moon rise and set times in UTC
    moon_rise_utc = observer.previous_rising(ephem.Moon())
    moon_set_utc = observer.next_setting(ephem.Moon())

    return moon_rise_utc, moon_set_utc

def convert_to_ist(time_utc):
    # Convert UTC time to IST using pytz
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = pytz.utc.localize(time_utc.datetime()).astimezone(ist_timezone)
    return ist_time

# Example usage
observer = ephem.Observer()
date = '2024-02-07'  # Replace with the date for which you want to calculate the moon rise and set times
moon_rise_utc, moon_set_utc = calculate_moon_rise_set(observer, date)

# Convert to IST
moon_rise_ist = convert_to_ist(moon_rise_utc)
moon_set_ist = convert_to_ist(moon_set_utc)

print(f'Moon Rise (UTC): {moon_rise_utc}')
print(f'Moon Set (UTC): {moon_set_utc}')

print(f'Moon Rise (IST): {moon_rise_ist}')
print(f'Moon Set (IST): {moon_set_ist}')



import ephem

def get_moon_angle(observer):
    # Create a Moon object
    moon = ephem.Moon()

    # Set the observer's location
    observer.date = ephem.now()
    
    # Compute the Moon's position
    moon.compute(observer)

    # Get the Moon's altitude and azimuth in radians
    altitude = moon.alt
    azimuth = moon.az

    # Convert altitude and azimuth to degrees
    altitude_deg = ephem.degrees(altitude)
    azimuth_deg = ephem.degrees(azimuth)

    return altitude_deg, azimuth_deg

# Example: Get Moon's angle for a specific location
observer = ephem.Observer()
observer.lat = '12.97'  # Latitude of a location
observer.lon = '77.56'  # Longitude of a location
moon_altitude, moon_azimuth = get_moon_angle(observer)

print(f'Moon Altitude: {moon_altitude} degrees')
print(f'Moon Azimuth: {moon_azimuth} degrees')


import ephem

def calculate_thithi(observer):
    # Create a Sun and Moon object
    sun = ephem.Sun()
    moon = ephem.Moon()

    # Set the observer's location
    observer.date = ephem.now()

    # Compute the Sun's and Moon's positions
    sun.compute(observer)
    moon.compute(observer)

    # Get the elongation angle (angle between Sun and Moon)
    elongation = (moon.hlong - sun.hlong) % 360.0

    # Calculate Thithi based on elongation
    thithi = (elongation // 12) + 1

    return int(thithi)

# Example: Calculate Thithi for a specific location
observer = ephem.Observer()
observer.lat = '12.97'  # Latitude of a location
observer.lon = '77.56'  # Longitude of a location

current_thithi = calculate_thithi(observer)

print(f'Current Thithi: {current_thithi}')


import ephem
import math

def calculate_nakshatra(observer):
    # Create a Moon object
    moon = ephem.Moon()

    # Set the observer's location
    observer.date = ephem.now()
    print(observer.date)

    # Compute the Moon's position
    l = moon.compute(observer)

    # Get the Moon's ecliptic longitude
    moon_longitude = moon.hlon
    print(f'Moon Longitude: {moon_longitude} degrees')
    print(type(moon_longitude))


    

    # Example ephem angle in radians
    ephem_angle_radians = ephem.degrees(moon_longitude)

    # Convert ephem angle to degrees
    moon_longitude= math.degrees(ephem_angle_radians)
    print(moon_longitude,"conversion")

    


    


    # Calculate Nakshatra based on the Moon's longitude
    nakshatra = (moon_longitude // 13.3333 ) -1
    print(f'Nakshatra Number: {int(nakshatra)}')

    return int(nakshatra)

def get_nakshatra_name(nakshatra_number):
    print(nakshatra_number,"first minus nak number")
    # Define Nakshatra names
    nakshatra_names = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
        "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
        "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
        "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
        "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
        "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ]

    # Return the corresponding Nakshatra name
    return nakshatra_names[nakshatra_number-1]

# Example: Print the name of the current Nakshatra for a specific location
observer = ephem.Observer()
observer.lat = '12.97'  # Latitude of a location
observer.lon = '77.56'  # Longitude of a location

current_nakshatra = calculate_nakshatra(observer)
nakshatra_name = get_nakshatra_name(current_nakshatra)

print(f'Current Nakshatra: {current_nakshatra} - {nakshatra_name}')

import ephem
from datetime import datetime
import pytz

def calculate_sunrise_sunset(observer, date):
    # Set the observer's location
    observer.date = date

    # Compute sunrise and sunset in UTC
    sunrise_utc = observer.previous_rising(ephem.Sun()).datetime()
    sunset_utc = observer.next_setting(ephem.Sun()).datetime()

    return sunrise_utc, sunset_utc

def convert_utc_to_ist(utc_time):
    # Define UTC and IST time zones
    utc_timezone = pytz.timezone('UTC')
    ist_timezone = pytz.timezone('Asia/Kolkata')

    # Convert UTC time to IST
    utc_time = utc_timezone.localize(utc_time)
    ist_time = utc_time.astimezone(ist_timezone)

    return ist_time

# Example: Calculate sunrise and sunset for a specific location and date
observer = ephem.Observer()
observer.lat = '12.97'  # Latitude of a location
observer.lon = '77.56'  # Longitude of a location

# Set the date for calculation
date_to_calculate = ephem.now()  # Use current date and time

# Calculate sunrise and sunset in UTC
sunrise_time_utc, sunset_time_utc = calculate_sunrise_sunset(observer, date_to_calculate)

# Convert UTC to IST
sunrise_time_ist = convert_utc_to_ist(sunrise_time_utc)
sunset_time_ist = convert_utc_to_ist(sunset_time_utc)

print(f'Sunrise (UTC): {sunrise_time_utc}')
print(f'Sunset (UTC): {sunset_time_utc}')

print(f'Sunrise (IST): {sunrise_time_ist}')
print(f'Sunset (IST): {sunset_time_ist}')




import ephem
import pytz
from datetime import datetime
from datetime import timedelta

def calculate_tithi(observer):
    # Create a Moon object
    moon = ephem.Moon()

    # Set the observer's location
    observer.date = "2024/2/7 07:18:45"
    observer.date
    #print(ephem.now(),"time of tithi")

    # Compute the Moon's position
    moon.compute(observer)

    # Get the date of the last new moon
    last_new_moon_date = ephem.previous_new_moon(observer.date)

    # Calculate the phase of the moon (days since the last new moon)
    moon_phase = observer.date - last_new_moon_date

    # Convert moon_phase to integer and take modulo 30
    tithi = int(moon_phase) % 30 + 1

    return tithi

# ... (rest of the code remains the same)


# ... (rest of the code remains the same)

def get_tithi_name(tithi_number):
    # Define Tithi names
    tithi_names = [
        "Pratipat", "Dvitiya", "Tritiya", "Chaturthi", "Panchami",
        "Shashti", "Saptami", "Ashtami", "Navami", "Dashami",
        "Ekadashi", "Dvadashi", "Trayodashi", "Chaturdashi", "Purnima",
        "Pratipat (Krishna)", "Dvitiya (Krishna)", "Tritiya (Krishna)", "Chaturthi (Krishna)", "Panchami (Krishna)",
        "Shashti (Krishna)", "Saptami (Krishna)", "Ashtami (Krishna)", "Navami (Krishna)", "Dashami (Krishna)",
        "Ekadashi (Krishna)", "Dvadashi (Krishna)", "Trayodashi (Krishna)", "Chaturdashi (Krishna)", "Amavasya"
    ]

    # Return the corresponding Tithi name
    return tithi_names[tithi_number - 1]

# Example: Print the current Tithi and its name for Bangalore in IST
def get_tithi_for_bangalore():
    # Bangalore's coordinates
    bangalore_location = {'latitude': 12.9716, 'longitude': 77.5946}

    # Create an observer
    observer = ephem.Observer()
    observer.lat = str(bangalore_location['latitude'])
    observer.lon = str(bangalore_location['longitude'])

    # Calculate Tithi
    current_tithi = calculate_tithi(observer)

    # Get Tithi name
    tithi_name = get_tithi_name(current_tithi)

    # Convert to IST
    utc_time = datetime.utcnow()
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = pytz.utc.localize(utc_time).astimezone(ist_timezone)

    print(f'Current Tithi in Bangalore (IST): {current_tithi} - {tithi_name} as of {ist_time}')

# Run the example
get_tithi_for_bangalore()
import ephem
import pytz
from datetime import datetime, timedelta

def calculate_tithi(observer):
    # Create a Moon object
    moon = ephem.Moon()

    # Set the observer's location
    observer.date = ephem.now()

    # Compute the Moon's position
    moon.compute(observer)

    # Get the date of the next new moon
    next_new_moon_date = ephem.localtime(ephem.next_new_moon(observer.date))

    # Convert observer.date to a datetime object
    observer_datetime = ephem.localtime(observer.date)

    # Calculate the phase of the moon (days until the next new moon)
    moon_phase = (next_new_moon_date - observer_datetime).days % 30

    # Calculate Tithi based on the Moon's phase
    tithi = int(moon_phase) + 1

    return tithi

def get_tithi_end_time(latitude, longitude):
    # Create an observer
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)

    # Calculate Tithi
    current_tithi = calculate_tithi(observer)

    # Get the end time of the current Tithi
    utc_time = datetime.utcnow()
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = pytz.utc.localize(utc_time).astimezone(ist_timezone)

    # Calculate the end time of the current Tithi
    next_tithi_start_time = ist_time + timedelta(days=30 - current_tithi)

    print(f'Purnima Tithi ends at: {next_tithi_start_time}')

# Example: Print the end time of Purnima Tithi for Bangalore in IST
get_tithi_end_time(12.9716, 77.5946)







