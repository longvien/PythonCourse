
city = input('Pls enter a city that u want to see the weather forecast\n')
import requests
link = "http://api.weatherapi.com/v1/current.json?key=49e46da730864097922165451250402&q=" + city + "&aqi=no"
response = requests.get(link)
data = response.json()
temp = data.get('current').get('temp_c')
print("It's now in", city, temp, "°C")