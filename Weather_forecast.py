import requests

# Local fallback data (for offline demo use)
local_data = {
    "delhi": {"temp": 31, "humidity": 40, "desc": "clear sky"},
    "bangalore": {"temp": 28, "humidity": 35, "desc": "partly cloudy"},
    "mumbai": {"temp": 32, "humidity": 70, "desc": "humid and warm"},
    "chennai": {"temp": 30, "humidity": 75, "desc": "light showers"},
}

def get_weather(city):
    """
    Attempts to fetch live weather data using OpenWeatherMap API.
    If no API key is available or an error occurs, falls back to local data.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = ""  # <-- Left empty for security (you can add yours locally if needed)

    if not api_key:
        # Fallback mode — use local predefined data
        print("⚠️ No API key detected. Using local weather data...\n")
        data = local_data.get(city.lower())
        if data:
            display_weather(city, data["temp"], data["humidity"], data["desc"])
        else:
            print("❌ City not found in local data.")
        return

    try:
        params = {"q": city, "appid": api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]
            display_weather(city, temp, humidity, desc)
        else:
            print("❌ City not found or API request failed.")
    except Exception as e:
        print("⚠️ Error fetching live data. Switching to local data...\n")
        data = local_data.get(city.lower())
        if data:
            display_weather(city, data["temp"], data["humidity"], data["desc"])
        else:
            print("❌ City not found in local data.")

def display_weather(city, temp, humidity, desc):
    """Neatly formats and prints the weather data."""
    print(f"\n🌤️ Weather Forecast for {city.title()}:")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌈 Condition: {desc.capitalize()}\n")

# Main app loop
while True:
    city = input("Enter the city name to view weather forecast: ").strip()
    get_weather(city)

    again = input("Do you want to check another city? (y/n): ").lower()
    if again != "y":
        print("Thank you for using the Weather App! ☀️")
        break
