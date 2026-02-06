import time
import os
import requests
from weather_hardware import blink_blue, blink_pink, idle_weather

# -----------------------------
# CONFIG
# -----------------------------
CITY = "San Juan,PR"
CHECK_INTERVAL = 1800  # 30 minutes

API_KEY = os.getenv("OPENWEATHER_API_KEY")
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

if not API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY not set")

# Weather types considered severe
SEVERE_KEYWORDS = [
    "rain",
    "drizzle",
    "thunderstorm",
    "storm",
    "snow"
]

# -----------------------------
# FUNCTIONS
# -----------------------------
def severe_weather_today():
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    for entry in data["list"]:
        condition = entry["weather"][0]["main"].lower()

        for keyword in SEVERE_KEYWORDS:
            if keyword in condition:
                return True

    return False


# -----------------------------
# MAIN LOOP
# -----------------------------
print("Weather Tracker Starting...")
idle_weather()

while True:
    try:
        print("Checking daily forecast...")

        if severe_weather_today():
            print("Rain or severe weather detected today")
            blink_pink()
        else:
            print("Clear weather all day")
            blink_blue()

        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("Weather Tracker stopped")
        idle_weather()
        break

    except Exception as e:
        print(f"Weather API error: {e}")
        idle_weather()
        time.sleep(300)
