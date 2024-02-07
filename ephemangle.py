# import ephem
# from datetime import datetime, timedelta

# def get_moon_phase(date, latitude, longitude):
#     observer = ephem.Observer()
#     observer.lat = str(latitude)  # Latitude of a location
#     observer.lon = str(longitude)  # Longitude of a location

#     # Create a Moon object
#     moon = ephem.Moon()

#     # Initialize the start and end dates of the lunar month
#     start_date = datetime.strptime(date, '%Y-%m-%d')
#     end_date = start_date + timedelta(days=29)

#     current_date = start_date
#     moon_phases = []

#     while current_date <= end_date:
#         observer.date = current_date.strftime('%Y-%m-%d')

#         # Compute the Moon's position
#         moon.compute(observer)

#         # Get the moon phase
#         phase = moon.phase
#         print(phase)

#         # Determine the moon phase category
#         if 0 <= phase < 7.4:
#             moon_phase = "New Moon"
#         elif 7.4 <= phase < 14.8:
#             moon_phase = "First Quarter"
#         elif 14.8 <= phase < 22.1:
#             moon_phase = "Full Moon"
#         else:
#             moon_phase = "Last Quarter"

#         moon_phases.append((current_date, moon_phase))

#         # Move to the next day
#         current_date += timedelta(days=1)

#     return moon_phases

# # Example usage
# date = '2024-02-01'
# latitude = 12.97
# longitude = 77.56

# lunar_month_phases = get_moon_phase(date, latitude, longitude)

# for phase_date, phase_name in lunar_month_phases:
#     print(f'{phase_date.strftime("%Y-%m-%d")}: {phase_name}')


# import ephem
# from datetime import datetime, timedelta

# def calculate_moon_phases_in_month(year, month, latitude, longitude):
#     observer = ephem.Observer()
#     observer.lat = str(latitude)  # Latitude of a location
#     observer.lon = str(longitude)  # Longitude of a location

#     # Create a Moon object
#     moon = ephem.Moon()

#     # Get the first date of the month
#     start_date = datetime(year, month, 1)

#     # Calculate the dates of the four primary moon phases within the month
#     moon_phases = []

#     for i in range(31):  # Assume a month with a maximum of 31 days
#         current_date = start_date + timedelta(days=i)
#         observer.date = current_date.strftime('%Y-%m-%d')

#         # Compute the Moon's position
#         moon.compute(observer)

#         # Get the Moon phase in degrees
#         phase = moon.phase

#         # Determine the Moon phase category
#         if 0 <= phase < 7.4:
#             moon_phase = "New Moon"
#         elif 7.4 <= phase < 14.8:
#             moon_phase = "First Quarter"
#         elif 14.8 <= phase < 22.1:
#             moon_phase = "Full Moon"
#         elif 22.1 <= phase < 29.5:
#             moon_phase = "Last Quarter"
#         else:
#             continue  # Skip other phases

#         moon_phases.append((current_date, moon_phase))

#     return moon_phases

# # Example usage
# year = 2024
# month = 2
# latitude = 12.97
# longitude = 77.56

# moon_phases_in_month = calculate_moon_phases_in_month(year, month, latitude, longitude)

# for phase_date, phase_name in moon_phases_in_month:
#     print(f'{phase_date.strftime("%Y-%m-%d")}: {phase_name}')
import ephem
import math
from datetime import datetime, timedelta

def calculate_nakshatra_times_for_day(date, latitude, longitude):
    observer = ephem.Observer()
    observer.lat = str(latitude)  # Latitude of a location
    observer.lon = str(longitude)  # Longitude of a location

    # Create a Moon object
    moon = ephem.Moon()

    # Set the date for which you want to calculate the Nakshatra
    observer.date = date

    # Initialize variables
    current_nakshatra = None
    start_time = None
    end_time = None

    # Set a maximum number of iterations to avoid an infinite loop
    max_iterations = 1000
    iteration_count = 0

    # Use a larger time step to iterate through the day
    time_step = ephem.hour * 10

    # Iterate through the day
    while ephem.localtime(observer.date).day == ephem.localtime(date).day and iteration_count < max_iterations:
        # Increment the iteration count
        iteration_count += 1

        # Compute the Moon's position
        moon.compute(observer)

        # Get the Moon's ecliptic longitude in degrees
        moon_longitude = math.degrees(moon.hlon)

        # Calculate Nakshatra based on the Moon's longitude
        new_nakshatra = int((moon_longitude + 360) // 13.3333) + 1

        if current_nakshatra is None:
            current_nakshatra = new_nakshatra
            start_time = ephem.localtime(observer.date)

        elif current_nakshatra != new_nakshatra:
            end_time = ephem.localtime(observer.date)
            break

        # Move time forward
        observer.date += time_step  # Adjust the time step as needed

    return start_time, end_time, current_nakshatra

def get_nakshatra_name(nakshatra_number):
    nakshatra_names = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
        "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
        "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
        "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
        "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
        "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ]
    return nakshatra_names[nakshatra_number - 1]

# Example: Calculate Nakshatra times for a particular date with latitude and longitude
date = '2024-02-15 00:00:00'  # Replace with the desired date and time
latitude = 12.97
longitude = 77.56

start_time, end_time, nakshatra_number = calculate_nakshatra_times_for_day(date, latitude, longitude)
nakshatra_name = get_nakshatra_name(nakshatra_number)

print(f'{nakshatra_name} Nakshatra on {date}:')
print(f'Start Time: {start_time}')
print(f'End Time: {end_time}')

