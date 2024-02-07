
# import ephem



# def calculate_nakshatra(moon_longitude):
#     # Convert Moon's ecliptic longitude to decimal degrees
#     moon_longitude_decimal = ephem.degrees(moon_longitude)

  

#     # Define Nakshatra boundaries in degrees (for reference)
#     nakshatra_boundaries = [
#         0.0, 13.3333, 26.6667, 40.0, 53.3333, 66.6667, 80.0,
#         93.3333, 106.6667, 120.0, 133.3333, 146.6667, 160.0,
#         173.3333, 186.6667, 200.0, 213.3333, 226.6667, 240.0,
#         253.3333, 266.6667, 280.0, 293.3333, 306.6667, 320.0,
#         333.3333, 346.6667
#     ]

#     # Find the Nakshatra based on Moon's ecliptic longitude
#     for i, boundary in enumerate(nakshatra_boundaries):
#         if moon_longitude_decimal < boundary:
#             nakshatra_number = i
#             break
#     else:
#         nakshatra_number = 27  # Moon longitude is in the last Nakshatra

#     return nakshatra_number + 1  # Adding 1 to start Nakshatra numbering from 1

# # Example usage:
# # Set the observer's location (optional)
# observer = ephem.Observer()
# observer.lat = '12.97'  # Latitude of a location
# observer.lon = '77.56'  # Longitude of a location

# # Set the date and time for which you want to find the Moon's position
# date_time_utc = '2024-02-15 12:00:00'  # Replace with the desired date and time in UTC
# observer.date = date_time_utc

# # Create a Moon object
# moon = ephem.Moon()

# # Compute the Moon's position
# moon.compute(observer)

# # Get the Moon's ecliptic longitude
# moon_longitude = moon.hlon
# print(moon_longitude)
# # Calculate the Nakshatra based on the Moon's ecliptic longitude
# nakshatra_number = calculate_nakshatra(moon_longitude)
# print(f'Nakshatra Number: {nakshatra_number}')


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
import math

def calculate_nakshatra(observer, date):
    # Create a Moon object
    moon = ephem.Moon()

    # Set the observer's location and date
    observer.date = date

    # Compute the Moon's position
    l = moon.compute(observer)

    # Get the Moon's ecliptic longitude
    moon_longitude = moon.hlon

    # Convert the Moon's ecliptic longitude to degrees
    moon_longitude_degrees = math.degrees(float(moon_longitude))

    # Calculate Nakshatra based on the Moon's longitude
    nakshatra = (moon_longitude_degrees // 13.3333 ) - 1

    return int(nakshatra)

def get_nakshatra_name(nakshatra_number):
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
    return nakshatra_names[nakshatra_number]

# Example: Print the name of the current Nakshatra for a specific location and date
def main():
    observer = ephem.Observer()
    observer.lat = '12.97'  # Latitude of a location
    observer.lon = '77.56'  # Longitude of a location

    # Input the date
    year = int(input("Enter the year (YYYY): "))
    month = int(input("Enter the month (MM): "))
    day = int(input("Enter the day (DD): "))

    # Create the date object
    date = ephem.Date((year, month, day))

    # Calculate Nakshatra
    current_nakshatra = calculate_nakshatra(observer, date)
    nakshatra_name = get_nakshatra_name(current_nakshatra)

    print(f'Nakshatra Number: {current_nakshatra}')
    print(f'Nakshatra Name: {nakshatra_name}')

if __name__ == "__main__":
    main()
2024