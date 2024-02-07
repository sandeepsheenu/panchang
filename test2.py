import ephem

def calculate_lunar_solar_longitude():
    # Set the observer's location (e.g., latitude and longitude for Bangalore)
    observer = ephem.Observer()
    observer.lat = '12.9716'
    observer.lon = '77.5946'

    # Compute the Moon's position
    moon = ephem.Moon(observer)
    print(moon)
    lunar_longitude = moon.ra  # Lunar longitude in radians
    print(lunar_longitude)
    # Compute the Sun's position
    sun = ephem.Sun(observer)
    solar_longitude = sun.ra  # Solar longitude in radians

    # Convert radians to degrees for better readability
    lunar_longitude_degrees = ephem.degrees(lunar_longitude)
    print(lunar_longitude_degrees,"in degree")
    solar_longitude_degrees = ephem.degrees(solar_longitude)
    print(solar_longitude_degrees,"in degree")

    # Add both longitudes and divide by 12
    total_longitude_degrees = (lunar_longitude_degrees + solar_longitude_degrees) 
    return total_longitude_degrees

def main():
    total_longitude = calculate_lunar_solar_longitude()

    print(f"Total Longitude: {total_longitude:.2f} degrees")

if __name__ == "__main__":
    main()



import ephem

def calculate_lunar_solar_longitude():
    # Set the observer's location (e.g., latitude and longitude for Bangalore)
    observer = ephem.Observer()
    observer.lat = '12.9716'
    observer.lon = '77.5946'

    # Compute the Moon's position
    moon = ephem.Moon(observer)
    moon.compute(observer)
    lunar_longitude = moon.ra  # Lunar longitude in radians

    # Compute the Sun's position
    sun = ephem.Sun(observer)
    sun.compute(observer)
    solar_longitude = sun.ra  # Solar longitude in radians

    # Convert radians to degrees for better readability
    lunar_longitude_degrees = ephem.degrees(lunar_longitude)
    solar_longitude_degrees = ephem.degrees(solar_longitude)

    # Add both longitudes and divide by 13 degrees and 20 minutes
    total_longitude_degrees = (lunar_longitude_degrees + solar_longitude_degrees) / ephem.degree
    total_longitude = ephem.degrees(total_longitude_degrees)

    return total_longitude

def main():
    total_longitude = calculate_lunar_solar_longitude()

    print(f"Total Longitude: {total_longitude}")

if __name__ == "__main__":
    main()


