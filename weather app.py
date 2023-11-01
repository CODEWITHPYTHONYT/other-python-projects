import requests
import os
import geocoder
import pyttsx3

# Replace with your WeatherAPI.com API key
api_key = "a0b2b19f9fd34f4fa56113221230910"

# Automatically detect the user's location
user_location = geocoder.ip("me")

# Get the city from the user's location
city = user_location.city

# Make a request to the WeatherAPI.com to get weather data
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
response = requests.get(url)
data = response.json()

# Check if the request was successful
if "error" in data:
    print(f"Error: {data['error']['message']}")
else:
    location = data["location"]
    current = data["current"]

    # Extract weather information
    condition = current["condition"]["text"]
    temperature = current["temp_c"]

    # Create a weather report string
    weather_report = f"In {location['name']}, it's currently {condition} with a temperature of {temperature} degrees Celsius."

    # Use pyttsx3 to say the weather report
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 180)
    print(f"A.I: {weather_report}")
    engine.say(weather_report)
    engine.runAndWait()
