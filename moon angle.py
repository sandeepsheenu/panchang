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
    nakshatra = (moon_longitude / 13.3333) % 27
    print(f'Nakshatra Number: {int(nakshatra)}')

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
    return nakshatra_names[nakshatra_number -1]

# Example: Print the name of the current Nakshatra for a specific location
observer = ephem.Observer()
observer.lat = '12.97'  # Latitude of a location
observer.lon = '77.56'  # Longitude of a location

current_nakshatra = calculate_nakshatra(observer)
nakshatra_name = get_nakshatra_name(current_nakshatra)

print(f'Current Nakshatra: {current_nakshatra} - {nakshatra_name}')
