import random
from datetime import datetime


def fetch_weather_data(city):
    # Simulated API response
    return {
        "city": city,
        "temp": random.randint(10, 30),
        "condition": random.choice(["sunny", "cloudy", "rainy"]),
        "humidity": random.randint(40, 80),
    }


def fetch_forecast(city, days=3):
    forecast = []
    for _ in range(days):
        forecast.append({
            "temp": random.randint(10, 30),
            "condition": random.choice(["sunny", "cloudy", "rainy"]),
        })
    return forecast


def get_current_hour():
    return datetime.now().hour
