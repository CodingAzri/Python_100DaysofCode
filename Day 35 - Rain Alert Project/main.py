import requests
import smtplib

MY_EMAIL = MY EMAIL
PASSWORD = PASSWORD
location = location
api_key = api key
OWM_Endpoint = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={(location)}&days=1&aqi=no&alerts=no"
rain_codes = [
    1150, 1153, 1168, 1171, 1180, 1183, 1186, 1189,
    1192, 1195, 1198, 1201, 1240, 1243, 1246, 1273, 1276
]

response = requests.get(OWM_Endpoint)
response.raise_for_status()
weather_data = response.json()

will_rain = False

hourly_forecast_slice = weather_data["forecast"]["forecastday"][0]["hour"][:12]
for hour_data in hourly_forecast_slice:
    condition_code = hour_data["condition"]["code"]
    if int(condition_code) in rain_codes:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Rain Alert!\n\nIt's going to rain today! Bring your umbrella :)"
                            )
