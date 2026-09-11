import requests
from config import API_KEY, BASE_URL


def get_current_weather(city, unit="metric"):

    url = f"{BASE_URL}/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": unit
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        print("API Status Code:", response.status_code)

        if response.status_code != 200:
            print("API Response:", response.text)

        if response.status_code == 401:
            raise Exception("Invalid or inactive API key")

        if response.status_code == 404:
            raise Exception("City not found")

        if response.status_code == 429:
            raise Exception("API request limit exceeded")

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        raise Exception("Request timed out")

    except requests.exceptions.ConnectionError:
        raise Exception("No internet connection")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Weather API error: {e}")