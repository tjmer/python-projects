import requests

def get_weather_desc_and_temp():
    api_key = "6c40a4117bd22810e4e1cbaf42404e7a"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    # print(json)

    description = json.get("weather")[0].get('description')
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max
    }

def main():
    weather_dict = get_weather_desc_and_temp()
    # Print the results
    print("Today's forcast is", weather_dict.get('description'))
    print("Minimum temperature is", weather_dict.get('temp_min'))
    print("Todays maximum temperature is", weather_dict.get('temp_max'))

main()