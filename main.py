# from weather_api import get_current_weather

# city = input("Enter city: ")

# try:
#     data = get_current_weather(city)

#     print(data)

# except Exception as e:
#     print("Error:", e)
import os
from dotenv import load_dotenv

load_dotenv()

print("Current folder:")
print(os.getcwd())

print("\nFiles in current folder:")
print(os.listdir())

print("\nAPI key:")
print(os.getenv("OPENWEATHER_API_KEY"))