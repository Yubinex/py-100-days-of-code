import requests
import datetime as dt
import smtplib

current_date = dt.datetime.now()
current_date_formatted = str(current_date).split()[0]
current_hour = current_date.hour

MY_EMAIL = "j.hauck1999@gmail.com"
PASSWORD = "srvbrxidcrzxtftb"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key: str = "69f04e4613056b159c2761a9d9e664d2"

parameters = {
    "lat": 49.1124645,
    "lon": 9.7372649,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

mail_content: str = f"Subject:12 Hour Weather Forecast for {current_date_formatted}\n\n"

will_rain = False

for index, item in enumerate(weather_slice):
    mail_content += f"{current_hour + (index+1)}:00 - {item['weather'][0].get('main')} -- {item['weather'][0].get('description')}\n"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="janhauck99@gmail.com",
                        msg=mail_content
                        )
