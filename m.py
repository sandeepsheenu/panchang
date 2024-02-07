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
    
    sun_rad = sun.ra  # Right ascension of the Sun in radians
    print(sun_rad, "rad sun")

# Example usage
latitude = 12.9716  # Latitude of Bangalore, India
longitude = 77.5946  # Longitude of Bangalore, India
date = ephem.now()  # Current date and time in UTC

calculate_yoga(latitude, longitude, date)
