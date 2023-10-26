import requests
from twilio.rest import Client

api_key = "f58c43ce04dfaf03dd2faffa027878ed"
account_sid = 'ACdab0e16809f628802d3c58f2bb87a742'
auth_token = '72c9b887c7f3a6e43682b85e3f873aa5'

api_call = f"https://api.openweathermap.org/data/2.8/onecall"
weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_call, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella☔️",
            from_='+12562865057',
            to='+234 902 858 8055'
        )
    print(message.status)
