import requests


def weatherApi():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=bd5eb5a061e1ee4ec5834ca1467fd5a6'
    city = 'Ireland'
    city_weather = requests.get(
        url.format(city)).json()  # request the API data and convert the JSON to Python data types
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    return weather
