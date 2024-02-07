# # import ephem
# # import math

# # def calculate_nakshatra(observer):
# #     # Create a Moon object
# #     moon = ephem.Moon()

# #     # Set the observer's location
# #     observer.date = ephem.now()
# #     print(observer.date)

# #     # Compute the Moon's position
# #     l = moon.compute(observer)

# #     # Get the Moon's ecliptic longitude
# #     moon_longitude = moon.hlon
# #     print(f'Moon Longitude: {moon_longitude} degrees')
# #     print(type(moon_longitude))


    

# #     # Example ephem angle in radians
# #     ephem_angle_radians = ephem.degrees(moon_longitude)

# #     # Convert ephem angle to degrees
# #     moon_longitude= math.degrees(ephem_angle_radians)
# #     print(moon_longitude,"conversion")

    


    


# #     # Calculate Nakshatra based on the Moon's longitude
# #     nakshatra = (moon_longitude / 13.3333) % 27
# #     print(f'Nakshatra Number: {int(nakshatra)}')

# #     return int(nakshatra)

# # def get_nakshatra_name(nakshatra_number):
# #     # Define Nakshatra names
# #     nakshatra_names = [
# #         "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
# #         "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
# #         "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
# #         "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
# #         "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
# #         "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
# #     ]

# #     # Return the corresponding Nakshatra name
# #     return nakshatra_names[nakshatra_number -1]

# # # Example: Print the name of the current Nakshatra for a specific location
# # observer = ephem.Observer()
# # observer.lat = '12.97'  # Latitude of a location
# # observer.lon = '77.56'  # Longitude of a location

# # current_nakshatra = calculate_nakshatra(observer)
# # nakshatra_name = get_nakshatra_name(current_nakshatra)

# # print(f'Current Nakshatra: {current_nakshatra} - {nakshatra_name}')


# ##########working code dont delete it the above of nakshatra







# import ephem
# import math
# from datetime import datetime, timedelta
# import pytz

# IST = pytz.timezone('Asia/Kolkata')

# def calculate_nakshatra(observer):
#     # Create a Moon object
#     moon = ephem.Moon()

#     # Set the observer's location
#     observer.date = ephem.now()
#     print(observer.date)

#     # Compute the Moon's position
#     l = moon.compute(observer)

#     # Get the Moon's ecliptic longitude
#     moon_longitude = moon.hlon
#     print(f'Moon Longitude: {moon_longitude} degrees')

#     # Convert moon longitude to degrees
#     moon_longitude_deg = math.degrees(float(moon_longitude))
#     print(f'Moon Longitude (degrees): {moon_longitude_deg}')

#     # Calculate Nakshatra based on the Moon's longitude
#     nakshatra = (moon_longitude_deg / 13.3333) % 27
#     print(f'Nakshatra Number: {int(nakshatra)}')

#     return int(nakshatra)

# def get_nakshatra_name(nakshatra_number):
#     # Define Nakshatra names
#     nakshatra_names = [
#         "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
#         "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
#         "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
#         "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
#         "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
#         "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
#     ]

#     # Return the corresponding Nakshatra name
#     return nakshatra_names[nakshatra_number - 1]

# def main():
#     # Get inputs for date and time in IST
#     date_input = input("Enter date in YYYY-MM-DD format (IST): ")
#     time_input = input("Enter time in HH:MM:SS format (IST): ")

#     # Parse input to create a datetime object
#     date_time_ist = datetime.strptime(date_input + ' ' + time_input, '%Y-%m-%d %H:%M:%S')
    
#     # Convert IST time to UTC
#     date_time_utc = date_time_ist.astimezone(pytz.utc)
    
#     # Create an observer
#     observer = ephem.Observer()
#     observer.lat = '12.97'  # Latitude of a location
#     observer.lon = '77.56'  # Longitude of a location
#     observer.date = date_time_utc

#     # Calculate current Nakshatra
#     current_nakshatra = calculate_nakshatra(observer)
#     nakshatra_name = get_nakshatra_name(current_nakshatra)

#     print(f'Nakshatra for {date_time_ist.strftime("%Y-%m-%d %H:%M:%S")} IST: {current_nakshatra} - {nakshatra_name}')

# if __name__ == "__main__":
#     main()


# import ephem
# import math
# from datetime import datetime
# import pytz

# IST = pytz.timezone('Asia/Kolkata')

# def calculate_nakshatra(observer):
#     # Create a Moon object
#     moon = ephem.Moon()

#     # Compute the Moon's position
#     l = moon.compute(observer)

#     # Get the Moon's ecliptic longitude
#     moon_longitude = moon.hlon

#     # Convert moon longitude to degrees
#     moon_longitude_deg = math.degrees(float(moon_longitude))
#     print(moon_longitude_deg)

#     # Calculate Nakshatra based on the Moon's longitude
#     nakshatra = (moon_longitude_deg / 13.3333) % 27

#     return int(nakshatra)

# def get_nakshatra_name(nakshatra_number):
#     # Define Nakshatra names
#     nakshatra_names = [
#         "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
#         "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
#         "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
#         "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
#         "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
#         "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
#     ]

#     # Return the corresponding Nakshatra name
#     return nakshatra_names[nakshatra_number - 1]

# def main():
#     # Create an observer for Bangalore, India
#     observer = ephem.Observer()
#     observer.lat = '12.9716'  # Latitude of Bangalore, India
#     observer.lon = '77.5946'  # Longitude of Bangalore, India

#     # Get current date and time in IST
#     current_time_ist = datetime.now(IST)

#     # Set observer's date and time
#     observer.date = current_time_ist

#     # Calculate current Nakshatra
#     current_nakshatra = calculate_nakshatra(observer)
#     nakshatra_name = get_nakshatra_name(current_nakshatra)

#     print(f'Nakshatra for {current_time_ist.strftime("%Y-%m-%d %H:%M:%S")} IST: {current_nakshatra} - {nakshatra_name}')

# if __name__ == "__main__":
#     main()
import ephem
from datetime import datetime, timedelta
import math

def calculate_nakshatra_boundaries(observer, date):
    moon = ephem.Moon()
    observer.date = date

    nakshatra_boundaries = {}
    prev_nakshatra = None

    for i in range(24 * 60):  # Iterate through each minute in a day
        observer.date += ephem.minute  # Move time forward by a minute
        moon.compute(observer)
        moon_longitude = math.degrees(float(moon.hlon))

        # Calculate current Nakshatra
        nakshatra = (moon_longitude / 13.3333) % 27

        # Check if Nakshatra boundary crossed
        if nakshatra != prev_nakshatra and prev_nakshatra is not None:
            nakshatra_boundaries[prev_nakshatra].append(ephem.Date(observer.date - ephem.minute))

        if nakshatra != prev_nakshatra:
            prev_nakshatra = nakshatra
            nakshatra_boundaries.setdefault(nakshatra, []).append(ephem.Date(observer.date))

    return nakshatra_boundaries


def main():
    observer = ephem.Observer()
    observer.lat = '12.9716'  # Latitude of Bangalore, India
    observer.lon = '77.5946'  # Longitude of Bangalore, India

    current_time = datetime.utcnow()

    nakshatra_boundaries = calculate_nakshatra_boundaries(observer, current_time)

    for nakshatra, boundaries in nakshatra_boundaries.items():
        print(f'Nakshatra {int(nakshatra)} boundaries:', boundaries)
        if boundaries:
            start_time = boundaries[0].datetime().strftime('%Y-%m-%d %H:%M:%S')
            if len(boundaries) > 1:
                end_time = boundaries[-1].datetime().strftime('%Y-%m-%d %H:%M:%S')
            else:
                end_time = start_time  # Same as start time if no transition occurs
            print(f'Nakshatra {int(nakshatra)}: Start - {start_time}, End - {end_time}')
        else:
            print(f'Nakshatra {int(nakshatra)}: Not transitioning during the specified period.')

if __name__ == "__main__":
    main()

