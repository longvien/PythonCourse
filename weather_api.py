city = input('Please enter a city that u want to see the weather forecast!\n')
import requests
url = 'http://api.weatherapi.com/v1/current.json?key=49e46da730864097922165451250402&q=' + city + '&aqi=no'
response = requests.get(url)
weather_json = response.json()


temp = weather_json.get('current').get('temp_c')
condition = weather_json.get('current').get('condition').get('text')
print("It's now in", city, temp, "°C and", condition)