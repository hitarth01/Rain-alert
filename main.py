import requests
import os
from twilio.rest import Client
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACda852c44e9e59bfd33b0a0805bf27b32"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat" : 28.535517,
    "lon" : 77.391029,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_id = data["hourly"][0]["weather"][0]["id"]
print(weather_id)
weather_for_12hrs = data["hourly"][0:12]
weather_code_list = [weather_for_12hrs[hour]["weather"][0]["id"] for hour in range(0,12)]
print(weather_code_list)
for code in weather_code_list:
    if code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="It's going to rain today. Don't forget to bring an ☂️.",
                     from_="+16109049679",
                     to="+919264914757"
                 )
        print(message.status)
        break
#print(data)
