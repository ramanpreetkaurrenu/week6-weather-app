from weather_api import get_current_weather
from waether_parser import parse_current_weather
from weather_dispaly import display_current_weather
import requests 

city = input("Enter city: ")
icons = {
    "Clear": "☀",
    "Clouds": "☁",
    "Rain": "🌧",
    "Snow": "❄",
    "Thunderstorm": "⛈",
    "Mist": "🌫"
}

try:
    data = get_current_weather(city)

    weather = parse_current_weather(data)

    display_current_weather(weather)

except Exception as e:
    print("Error:", e)


while True:

    print("\n1. Current Weather")
    print("2. 5-Day Forecast")
    print("3. Change Unit")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pass

    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        break

    else:
        print("Invalid choice")
icon = icons.get(weather["condition"], "🌡")
