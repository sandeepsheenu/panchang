from flask import Flask, request, jsonify
import ephem
from datetime import datetime
import pytz

app = Flask(__name__)

# Secret API key
API_KEY = "sandeep123"

def calculate_sunrise_sunset(observer, date):
    observer.date = date
    sunrise_utc = observer.previous_rising(ephem.Sun()).datetime()
    sunset_utc = observer.next_setting(ephem.Sun()).datetime()
    return sunrise_utc, sunset_utc

def convert_utc_to_ist(utc_time):
    utc_timezone = pytz.timezone('UTC')
    ist_timezone = pytz.timezone('Asia/Kolkata')
    utc_time = utc_timezone.localize(utc_time)
    ist_time = utc_time.astimezone(ist_timezone)
    return ist_time

@app.route('/sunrise_sunset', methods=['GET'])
def get_sunrise_sunset():
    # Check for the presence of the API key
    api_key = request.args.get('api_key')
    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    # Get latitude and longitude from the request
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({'error': 'Latitude and Longitude are required'}), 400

    observer = ephem.Observer()
    observer.lat = lat
    observer.lon = lon

    date_to_calculate = ephem.now()
    sunrise_time_utc, sunset_time_utc = calculate_sunrise_sunset(observer, date_to_calculate)

    sunrise_time_ist = convert_utc_to_ist(sunrise_time_utc)
    sunset_time_ist = convert_utc_to_ist(sunset_time_utc)

    result = {
        'sunrise_utc': str(sunrise_time_utc),
        'sunset_utc': str(sunset_time_utc),
        'sunrise_ist': str(sunrise_time_ist),
        'sunset_ist': str(sunset_time_ist)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
