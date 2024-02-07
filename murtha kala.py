# import ephem
# from datetime import datetime, timedelta

# def calculate_timings(latitude, longitude, date):
#     observer = ephem.Observer()
#     observer.lat = str(latitude)
#     observer.lon = str(longitude)
#     observer.date = date

#     # Calculate sunrise and sunset
#     sunrise = ephem.localtime(observer.previous_rising(ephem.Sun())).replace(tzinfo=None)
#     sunset = ephem.localtime(observer.next_setting(ephem.Sun())).replace(tzinfo=None)
#     total_daylight_duration = (sunset - sunrise).total_seconds() / 3600.0

#     # Calculate Abhijit Muhurat
#     abhijit_muhurat_start = sunrise + timedelta(hours=(total_daylight_duration / 15) * 7.5)
#     abhijit_muhurat_end = sunrise + timedelta(hours=(total_daylight_duration / 15) * 8.5)

#     # Calculate Rahu Kala
#     rahu_kala_start = sunrise + timedelta(hours=(total_daylight_duration / 8) * 6)
#     rahu_kala_end = sunrise + timedelta(hours=(total_daylight_duration / 8) * 7)

#     # Calculate Amrit Kaal
#     amrit_kaal_start = sunrise + timedelta(hours=(total_daylight_duration / 8) * 3)
#     amrit_kaal_end = sunrise + timedelta(hours=(total_daylight_duration / 8) * 4)

#     # Calculate Yamagandam
#     yamagandam_start = sunrise + timedelta(hours=(total_daylight_duration / 8) * 5)
#     yamagandam_end = sunrise + timedelta(hours=(total_daylight_duration / 8) * 6)

#     # Calculate Varjyam
#     varjyam_start = sunrise + timedelta(hours=8)  # Assuming Varjyam starts 8 hours from sunrise
#     varjyam_end = sunrise + timedelta(hours=10)  # Assuming Varjyam lasts for 2 hours

#     # Calculate Dur Muhurtam
#     dur_muhurtam_start = sunrise + timedelta(hours=2)  # Assuming Dur Muhurtam starts 2 hours from sunrise
#     dur_muhurtam_end = sunrise + timedelta(hours=3)  # Assuming Dur Muhurtam lasts for 1 hour

#     return (
#         abhijit_muhurat_start, abhijit_muhurat_end,
#         rahu_kala_start, rahu_kala_end,
#         amrit_kaal_start, amrit_kaal_end,
#         yamagandam_start, yamagandam_end,
#         varjyam_start, varjyam_end,
#         dur_muhurtam_start, dur_muhurtam_end
#     )

# # Example: Calculate timings for Bangalore on a specific date
# latitude = 12.9716
# longitude = 77.5946
# date = ""  # Format: "YYYY-MM-DD"
# timings = calculate_timings(latitude, longitude, date)

# print(f"Abhijit Muhurat: {timings[0]} to {timings[1]}")
# print(f"Rahu Kala: {timings[2]} to {timings[3]}")
# print(f"Amrit Kaal: {timings[4]} to {timings[5]}")
# print(f"Yamagandam: {timings[6]} to {timings[7]}")
# print(f"Varjyam: {timings[8]} to {timings[9]}")
# print(f"Dur Muhurtam: {timings[10]} to {timings[11]}")

import ephem
from datetime import datetime, timedelta
import pytz

def calculate_timings(latitude, longitude, date):
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)
    observer.date = date

    # Calculate sunrise and sunset
    sunrise = ephem.localtime(observer.previous_rising(ephem.Sun())).replace(tzinfo=None)
    sunset = ephem.localtime(observer.next_setting(ephem.Sun())).replace(tzinfo=None)
    total_daylight_duration = (sunset - sunrise).total_seconds() / 3600.0

    # Calculate Abhijit Muhurat
    abhijit_muhurat_start = sunrise + timedelta(hours=(total_daylight_duration / 15) * 7.5)
    abhijit_muhurat_end = sunrise + timedelta(hours=(total_daylight_duration / 15) * 8.5)

    # Calculate Rahu Kala
    rahu_kala_start = sunrise + timedelta(hours=(total_daylight_duration / 8) * 6)
    rahu_kala_end = sunrise + timedelta(hours=(total_daylight_duration / 8) * 7)

    # Calculate Amrit Kaal
    amrit_kaal_start = sunrise + timedelta(hours=(total_daylight_duration / 8) * 3)
    amrit_kaal_end = sunrise + timedelta(hours=(total_daylight_duration / 8) * 4)

    # Calculate Yamagandam
    yamagandam_start = sunrise + timedelta(hours=(total_daylight_duration / 8) * 5)
    yamagandam_end = sunrise + timedelta(hours=(total_daylight_duration / 8) * 6)

    # Calculate Varjyam
    varjyam_start = sunrise + timedelta(hours=8)  # Assuming Varjyam starts 8 hours from sunrise
    varjyam_end = sunrise + timedelta(hours=10)  # Assuming Varjyam lasts for 2 hours

    # Calculate Dur Muhurtam
    dur_muhurtam_start = sunrise + timedelta(hours=2)  # Assuming Dur Muhurtam starts 2 hours from sunrise
    dur_muhurtam_end = sunrise + timedelta(hours=3)  # Assuming Dur Muhurtam lasts for 1 hour

    # Convert to IST time zone
    ist_timezone = pytz.timezone('Asia/Kolkata')
    abhijit_muhurat_start = ist_timezone.localize(abhijit_muhurat_start)
    abhijit_muhurat_end = ist_timezone.localize(abhijit_muhurat_end)
    rahu_kala_start = ist_timezone.localize(rahu_kala_start)
    rahu_kala_end = ist_timezone.localize(rahu_kala_end)
    amrit_kaal_start = ist_timezone.localize(amrit_kaal_start)
    amrit_kaal_end = ist_timezone.localize(amrit_kaal_end)
    yamagandam_start = ist_timezone.localize(yamagandam_start)
    yamagandam_end = ist_timezone.localize(yamagandam_end)
    varjyam_start = ist_timezone.localize(varjyam_start)
    varjyam_end = ist_timezone.localize(varjyam_end)
    dur_muhurtam_start = ist_timezone.localize(dur_muhurtam_start)
    dur_muhurtam_end = ist_timezone.localize(dur_muhurtam_end)

    return (
        abhijit_muhurat_start, abhijit_muhurat_end,
        rahu_kala_start, rahu_kala_end,
        amrit_kaal_start, amrit_kaal_end,
        yamagandam_start, yamagandam_end,
        varjyam_start, varjyam_end,
        dur_muhurtam_start, dur_muhurtam_end
    )

# Example: Calculate timings for Bangalore on a specific date
latitude = 12.9716
longitude = 77.5946
date = "2024-02-05"  # Format: "YYYY-MM-DD"
timings = calculate_timings(latitude, longitude, date)

print(f"Abhijit Muhurat: {timings[0]} to {timings[1]}")
print(f"Rahu Kala: {timings[2]} to {timings[3]}")
print(f"Amrit Kaal: {timings[4]} to {timings[5]}")
print(f"Yamagandam: {timings[6]} to {timings[7]}")
print(f"Varjyam: {timings[8]} to {timings[9]}")
print(f"Dur Muhurtam: {timings[10]} to {timings[11]}")

