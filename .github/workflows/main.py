import requests
from twilio.rest import Client
import os

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

Client()

weather_params = {
    "lat":17.393989,
    "lon":78.447261,
    "appid":api_key,
    "cnt":4
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()

print(response.status_code)

data = response.json()

print("List lenght: ", len(data))

will_rain = False
for index in range(len(data)-1):
    weather_id = data["list"][index]["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔️ ",
            from_="+19382533102",
            to="+52 81 3044 6650",
    )
    print(message.status)
