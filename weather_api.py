class Weather:
    def __init__(self, city, temperature, condition):
        self.city = city
        self.temp = temperature
        self.con = condition
    def output(self):
        print("It's now in " + self.city + ' ' + str(self.temp) + ' °C and ' + self.con)

choice = input('Please enter a city that you want to see the weather forecast!\n')

import requests
link = 'http://api.weatherapi.com/v1/current.json?key=49e46da730864097922165451250402&q=' + choice + '&aqi=no'
answer = requests.get(link)
data = answer.json()
if not choice or 'error' in data:
    print("City not found. Please try again.")
    exit()
else:
    city = data.get('location').get('name')
    temp = data.get('current').get('temp_c')
    condi = data.get('current').get('condition').get('text')
    my_forecast = Weather(city, temp, condi)
    my_forecast.output()
# city = input('Please enter a city that u want to see the weather forecast!\n')
# import requests
# url = 'http://api.weatherapi.com/v1/current.json?key=49e46da730864097922165451250402&q=' + city + '&aqi=no'
# response = requests.get(url)
# weather_json = response.json()
# 
# 
# temp = weather_json.get('current').get('temp_c')
# condition = weather_json.get('current').get('condition').get('text')
# print("It's now in", city, temp, "°C and", condition)