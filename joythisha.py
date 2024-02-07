# Import necessary modules and classes
from jyotisha.panchaanga.temporal import City, Date, DailyPanchaanga, ComputationSystem

# Set up required parameters
city = City.get_city('Bangalore')  # Example: Set the city (you can replace 'New York' with your desired city)
date = Date(2024, 2, 6)  # Example: Set the date (year, month, day)
computation_system = ComputationSystem.DEFAULT  # Example: Set the computation system

# Create an instance of DailyPanchaanga
daily_panchaanga = DailyPanchaanga(city=city, date=date, computation_system=computation_system)

# Access desired Panchanga details
# For example, to access sunrise time:
sunrise_time = daily_panchaanga.jd_sunrise
print("Sunrise Time:", sunrise_time)

# You can similarly access other Panchanga details such as sunset time, moonrise time, moonset time, etc.
