import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch sensitive data from environment variables
my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")
api_key = os.getenv("API_KEY")
to_email = os.getenv("TO_EMAIL")

# OpenWeatherMap API endpoint for weather forecast
weather_map_endpoint = "http://api.openweathermap.org/data/2.5/forecast?"

# Parameters for the weather API request
params = {
    "lat": 51.507351,  # Latitude for London
    "lon": -0.127758,  # Longitude for London
    "appid": api_key,  # API key for authentication
    "cnt": 4,  # Number of forecast data points to retrieve
}

# Sending a GET request to the weather API
response = requests.get(url=weather_map_endpoint, params=params)

# Check the response status code
print(response.status_code)

# Parse the weather data from the response
weather_data = response.json()["list"]

# Loop through each weather data point
for weather in weather_data:
    weather_condition_id = weather["weather"][0]["id"]

    # Check if the weather condition indicates rain or bad weather
    if weather_condition_id > 700:
        # Send an email notification if the weather condition requires an umbrella
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Start TLS encryption for security
            connection.login(user=my_email, password=my_password)  # Login to the email account
            connection.sendmail(
                from_addr=my_email,  # Sender's email address
                to_addrs=to_email,  # Recipient's email address
                msg="Subject: Today Weather Update\n\nHello Mostafa,\nPlease bring an umbrella today due to rainy weather."
            )
        print("Message Sended Successfuly.")
        break  # Exit the loop after sending the email









