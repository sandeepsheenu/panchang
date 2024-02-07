import ephem

# Function to calculate the Yoga
def calculate_yoga(latitude, longitude, date):
    # Create an observer object
    observer = ephem.Observer()
    observer.lat = str(latitude)  # Latitude in degrees
    observer.lon = str(longitude)  # Longitude in degrees
    observer.date = date  # Date in UTC

    # Compute the positions of the Sun and the Moon
    sun = ephem.Sun(observer)
    moon = ephem.Moon(observer)

    # Calculate the positions
    sun.compute(observer)
    moon.compute(observer)
    sun_rad=float(sun.ra)
    print(sun_rad,"rad sun")
    degree_sun=(sun_rad)/ephem.degree
    print(degree_sun,"degree_sun")
    
    moon_rad=moon.ra

    print(moon_rad)


    # Get the longitudes of the Sun and the Moon in degrees
    sun_longitude_deg = float(sun.ra) / ephem.degree
    print(sun_longitude_deg)
    moon_longitude_deg = float(moon.ra) / ephem.degree
    print(moon_longitude_deg)

    # Calculate the Yoga
   # yoga_deg = (moon_longitude_deg + sun_longitude_deg) / 13 + ((moon_longitude_deg + sun_longitude_deg) % 13) * 20 /60
    yoga_deg = (moon_longitude_deg + sun_longitude_deg) / (13 + 20/60)

    print(yoga_deg)
    yoga_index = int(yoga_deg) % 27  # Ensure the index stays within the range of 27 Yogas
    print(yoga_index,"m")

    # List of Yogas
    yogas = ["Vishkumbh", "Preeti", "Aayushman", "Saubhagya", "Shobhan", "Atigand", "Sukarma", "Dhriti",
             "Shool", "Gand", "Vridhi", "Dhruv", "Vyaghat", "Harshan", "Vajra", "Sidhi", "Vyatipat", "Variyaan",
             "Parigh", "Shiv", "Sidh", "Sadhya", "Shubh", "Shukla", "Brahm", "Ainder", "Vaidhriti"]

    # Return the Yoga
    return yogas[yoga_index -1]

# Example usage
latitude = 12.9716  # Latitude of Bangalore, India
longitude = 77.5946  # Longitude of Bangalore, India
date = ephem.now()  
print(date)# Current date and time in UTC

yoga = calculate_yoga(latitude, longitude, date)
print("Yoga for the given date and location is:", yoga)



