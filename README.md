
# Weather Notification Script

This Python script fetches the weather forecast for London from the OpenWeatherMap API and sends an email notification if the weather indicates rain or bad weather.

## Features
- Fetches weather data from OpenWeatherMap API.
- Checks weather conditions and sends an email if rain is expected.
- Sends a notification email to a specified email address.

## Prerequisites
- Python 3.x
- Required Python packages:
  - `requests`
  - `smtplib`
  - `python-dotenv`

## Setup

### 1. Install the required dependencies:
You can install the necessary dependencies using `pip`. Run the following command:

```bash
pip install requests python-dotenv
```
2. Create a .env file:
In the root directory of the project, create a .env file to store your sensitive data. The .env file should look like this:
makefile
```python
EMAIL=your_email@gmail.com
PASSWORD=your_email_password
API_KEY=your_openweathermap_api_key
TO_EMAIL=recipient_email@example.com
```

4. Update the script with your values:
Make sure that your .env file contains the correct values for EMAIL, PASSWORD, API_KEY, and TO_EMAIL.

5. Run the script:
Once everything is set up, you can run the script using:
```python
python main.py
```
