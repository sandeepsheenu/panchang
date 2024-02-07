# from datetime import datetime, timedelta

# # Function to calculate Abhijeet Muhurta
# def calculate_abhijeet_muhurta(sunrise, sunset):
#     # Total duration between sunrise and sunset
#     total_duration = sunset - sunrise

#     # Duration of each muhurta (approximately 48 minutes)
#     muhurta_duration = total_duration / 15

#     # Abhijeet Muhurta starts from sunrise and continues for 48 minutes
#     abhijeet_muhurta_start = sunrise
#     abhijeet_muhurta_end = abhijeet_muhurta_start + timedelta(minutes=48)

#     # Print Abhijeet Muhurta timings
#     print("Abhijeet Muhurta Timings:")
#     for i in range(8):
#         print("Muhurta {}: {} to {}".format(i+1, abhijeet_muhurta_start.strftime('%H:%M'), abhijeet_muhurta_end.strftime('%H:%M')))
#         abhijeet_muhurta_start = abhijeet_muhurta_end
#         abhijeet_muhurta_end += muhurta_duration

# # Example usage
# if __name__ == "__main__":
#     # Input sunrise and sunset times (replace with actual times)
#     sunrise = datetime.strptime("06:44", "%H:%M")  # Example: 6:30 AM
#     sunset = datetime.strptime("18:23", "%H:%M")   # Example: 6:30 PM

#     # Calculate Abhijeet Muhurta
#     calculate_abhijeet_muhurta(sunrise, sunset)
from datetime import datetime, timedelta

# Function to calculate Abhijeet Muhurta
def calculate_abhijeet_muhurta(sunrise, sunset):
    # Total duration between sunrise and sunset
    total_duration = sunset - sunrise

    # Duration of each part
    part_duration = total_duration / 15

    # Abhijeet Muhurta is the 8th part
    abhijeet_muhurta_start = sunrise + (7 * part_duration)
    abhijeet_muhurta_end = abhijeet_muhurta_start + part_duration

    # Print Abhijeet Muhurta timings
    print("Abhijeet Muhurta Timings:")
    print("From:", abhijeet_muhurta_start.strftime('%H:%M'))
    print("To:", abhijeet_muhurta_end.strftime('%H:%M'))

# Example usage
if __name__ == "__main__":
    # Input sunrise and sunset times (replace with actual times)
    sunrise = datetime.strptime("06:45", "%H:%M")  # Example: 6:30 AM
    sunset = datetime.strptime("18:23", "%H:%M")   # Example: 6:30 PM

    # Calculate Abhijeet Muhurta
    calculate_abhijeet_muhurta(sunrise, sunset)
