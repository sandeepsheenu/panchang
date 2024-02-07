import ephem
import pytz
from datetime import datetime

def calculate_tithi(observer, user_date_time):
    # Create a Moon object
    moon = ephem.Moon()

    # Set the observer's location
    observer.date = user_date_time

    # Compute the Moon's position
    moon.compute(observer)

    # Get the date of the last new moon
    last_new_moon_date = ephem.previous_new_moon(observer.date)

    # Calculate the phase of the moon (days since the last new moon)
    moon_phase = observer.date - last_new_moon_date

    # Convert moon_phase to integer and take modulo 30
    tithi = int(moon_phase) % 30 + 1

    return tithi

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

def get_tithi_for_location(latitude, longitude, user_date_time):
    # Create an observer
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)

    # Calculate Tithi
    current_tithi = calculate_tithi(observer, user_date_time)

    # Get Tithi name
    tithi_name = get_tithi_name(current_tithi)

    return current_tithi, tithi_name

# Example usage: Get Tithi for a specific location and user-input date and time
def get_tithi_for_user_input():
    # Get user input for date and time
    user_date_time_str = input("Enter the date and time (YYYY/MM/DD HH:MM:SS): ")
    user_date_time = ephem.Date(user_date_time_str)

    # Get user input for location (latitude and longitude)
    latitude = float(input("Enter the latitude of the location: "))
    longitude = float(input("Enter the longitude of the location: "))

    # Get Tithi for the provided location and user-input date and time
    tithi, tithi_name = get_tithi_for_location(latitude, longitude, user_date_time)

    print(f'Current Tithi: {tithi} - {tithi_name}')

# Run the example
get_tithi_for_user_input()
