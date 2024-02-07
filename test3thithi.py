
import ephem
from datetime import datetime, timedelta

def calculate_tithi(date):
    observer = ephem.Observer()
    observer.date = date
    
    # Find the time of the previous and next new moon
    previous_new_moon = ephem.previous_new_moon(date)
    next_new_moon = ephem.next_new_moon(date)
    
    # Calculate the phase angle of the Moon (angle between the Moon and the Sun)
    moon = ephem.Moon(observer)
    sun = ephem.Sun(observer)
    phase_angle = ephem.separation(moon, sun)
    
    # Calculate the Tithi
    tithi = (phase_angle / ephem.degree) % 30 + 1
    
    return int(tithi)

# Example usage
date_str = "2024-01-31"  # Replace with your desired date
start_time = datetime.strptime(date_str, "%Y-%m-%d")

for hour in range(24):
    current_time = start_time + timedelta(hours=hour)
    tithi = calculate_tithi(current_time)
    print(f"At {current_time.strftime('%Y-%m-%d %H:%M:%S')}, Tithi is {tithi}")



import ephem
from datetime import datetime, timedelta

def calculate_tithi(date):
    observer = ephem.Observer()
    observer.date = date
    
    # Find the time of the previous and next new moon
    previous_new_moon = ephem.previous_new_moon(date)
    next_new_moon = ephem.next_new_moon(date)
    
    # Calculate the longitudes of the Moon and the Sun
    moon_longitude = ephem.Moon(observer).lon
    sun_longitude = ephem.Sun(observer).lon
    
    # Calculate the difference in longitudes
    delta_longitude = (moon_longitude - sun_longitude) % 360.0
    
    # Calculate the Tithi
    tithi = (delta_longitude / 12.0) % 30 + 1
    
    return int(tithi)

# Example usage
date_str = "2024-01-31"  # Replace with your desired date
start_time = datetime.strptime(date_str, "%Y-%m-%d")

for hour in range(24):
    current_time = start_time + timedelta(hours=hour)
    tithi = calculate_tithi(current_time)
    print(f"At {current_time.strftime('%Y-%m-%d %H:%M:%S')}, Tithi is {tithi}")