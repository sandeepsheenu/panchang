import ephem
from datetime import datetime, timedelta

def calculate_brahma_muhurta(date, latitude, longitude):
    # Observer
    obs = ephem.Observer()
    obs.date = date
    obs.lat = str(latitude)
    obs.long = str(longitude)

    # Get sunrise time
    sunrise = obs.previous_rising(ephem.Sun())
    print(sunrise)
    sunset=obs.next_setting(ephem.Sun())
    print(sunset)

    # Calculate Brahma Muhurta
    brahma_muhurta_start = ephem.localtime(sunrise) - timedelta(hours=1, minutes=36)
    brahma_muhurta_end = ephem.localtime(sunrise) - timedelta(minutes=48)  # 1 hour 36 minutes before sunrise

    #prathya sandhya
    prathah_sandhya_start= ephem.localtime(sunrise) - timedelta( minutes=48)
    prathah_sandhya_end=ephem.localtime(sunrise) + timedelta( minutes=24)

    #sayanah sandhya-
    sayanah_sandhya_start=ephem.localtime(sunset) -timedelta(minutes=24)
    sayanah_sandhya_end=ephem.localtime(sunset) +timedelta(minutes=48)



    return brahma_muhurta_start, brahma_muhurta_end ,prathah_sandhya_start,prathah_sandhya_end, sayanah_sandhya_start, sayanah_sandhya_end

# Input date, latitude, and longitude
date_input =  ephem.now()#input("Enter the date in YYYY-MM-DD format: ")
latitude_input = float(input("Enter the latitude in degrees: "))
longitude_input = float(input("Enter the longitude in degrees: "))

# Convert input date to datetime object
date = datetime.strptime(date_input, "%Y-%m-%d")

# Calculate Brahma Muhurta
brahma_muhurta_start, brahma_muhurta_end ,prathah_sandhya_start, prathah_sandhya_end,sayanah_sandhya_start,sayanah_sandhya_end= calculate_brahma_muhurta(date, latitude_input, longitude_input)

# Print result
print("Brahma Muhurta starts at:", brahma_muhurta_start.strftime("%Y-%m-%d %H:%M:%S"))
print("Brahma Muhurta ends at:", brahma_muhurta_end.strftime("%Y-%m-%d %H:%M:%S"))
print("prathah_sandhya_start at:", prathah_sandhya_start.strftime("%Y-%m-%d %H:%M:%S"))
print("prathah_sandhya_end at:", prathah_sandhya_end.strftime("%Y-%m-%d %H:%M:%S"))
print("sayanah_sandhya_start at:", sayanah_sandhya_start.strftime("%Y-%m-%d %H:%M:%S"))
print("sayanah_sandhya_end at:", sayanah_sandhya_end.strftime("%Y-%m-%d %H:%M:%S"))
