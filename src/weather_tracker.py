import time
import os
import requests
from weather_hardware import blink_blue_continuous, blink_pink_continuous, idle_weather

# -----------------------------
# CONFIG
# -----------------------------
CITY = "San Juan,PR"
CHECK_INTERVAL = 300  # 5 minutes

API_KEY = os.getenv("OPENWEATHER_API_KEY")
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

if not API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY not set")

SEVERE_KEYWORDS = ["rain", "drizzle", "thunderstorm", "storm", "snow"]

# -----------------------------
# FUNCTIONS
# -----------------------------
def severe_today():
    """Check full-day forecast for severe weather"""
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

current_status = None  # None, "severe", or "clear"

try:
    while True:
        try:
            if severe_today():
                if current_status != "severe":
                    current_status = "severe"
                    print("Severe weather detected today → Pink LED blinking")
                    blink_pink_continuous(lambda: current_status != "severe")
            else:
                if current_status != "clear":
                    current_status = "clear"
                    print("Clear weather all day → Blue LED blinking")
                    blink_blue_continuous(lambda: current_status != "clear")

            time.sleep(CHECK_INTERVAL)

        except requests.RequestException as e:
            print(f"Weather API error: {e}")
            idle_weather()
            time.sleep(60)

except KeyboardInterrupt:
    print("Weather Tracker stopped by user")
    idle_weather()
