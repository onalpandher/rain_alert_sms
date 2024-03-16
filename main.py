import requests
from twilio.rest import Client

apii_key="4759c4faf632872603215bf207217c07"
account_sid="ACe783f5b6d8204c36aa481612950f58ae"
auth_token="00772b6f21af3b7789d51982b0edcbc9"

parameter={
    "lat":30.900965,
    "lon":75.857277,
    "appid":apii_key,
    "cnt":4,
}

will_rain=False
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast" ,params=parameter)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])  #to reach that particular
for hour_data in weather_data["list"]:                #instead we will loop through all the ids of the day                                                       # which we gonna get evry 3 hours
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain=True
if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="Hello Carry Your Umbrella..It's gonna rain Today*_*",
        from_="+18646643125",
        to="+919988600716"
    )
    print(message.status)