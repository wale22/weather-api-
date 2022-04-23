import json
import requests

API_KEY="6e6a21917677e40e01554b1c5b63ad37"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

country=input("input the city name : ")

request_url=f'{BASE_URL}?appid={API_KEY}&q={country}'

responses=requests.get(request_url)

if responses.status_code == 200:
    result=responses.json()
    weather=result['weather'][0]['description']
    temperature=str(round(result['main']['temp']-273)) + ' celcius'
    print( weather)
    print(temperature)

else:
    print('an error occured')