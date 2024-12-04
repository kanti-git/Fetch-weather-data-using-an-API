import requests

def get_weather_data(city_name, api_key):
    """
    Fetches the current weather data for a given city using OpenWeatherMap API.

    Parameters:
        city_name (str): Name of the city to fetch the weather for.
        api_key (str): API key for OpenWeatherMap.

    Returns:
        dict: Weather data if successful, or error message if failed.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": "11ed486b825b04fd5910daeb6c1d6c0e",  # This is where the API key is used
        "units": "metric"  # For temperature in Celsius, use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "11ed486b825b04fd5910daeb6c1d6c0e"  # Replace this line with your API key
    city_name = input("Enter the city name: ")
    
    weather_data = get_weather_data(city_name, api_key)
    
    if "error" in weather_data:
        print("Error:", weather_data["error"])
    else:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

if __name__ == "__main__":
    main()

