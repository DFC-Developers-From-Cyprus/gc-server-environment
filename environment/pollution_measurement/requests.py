import os
import requests

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


def get_air_quality(location):
    url = f"https://api.waqi.info/feed/{location}/?token={TOKEN}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        return {"error": "API returned error"}

    iaqi = data["data"].get("iaqi", {})
    timestamp = data["data"].get("time", {}).get("iso", "unknown")

    sensor_meta = {
        "pm25": {
            "name": "PM2.5",
            "type": "pollutant",
            "sensor_type": "chemical",
            "unit": "AQI",
        },
        "pm10": {
            "name": "PM10",
            "type": "pollutant",
            "sensor_type": "chemical",
            "unit": "AQI",
        },
        "o3": {
            "name": "O3",
            "type": "pollutant",
            "sensor_type": "chemical",
            "unit": "AQI",
        },
        "no2": {
            "name": "NO2",
            "type": "pollutant",
            "sensor_type": "chemical",
            "unit": "AQI",
        },
        "so2": {
            "name": "SO2",
            "type": "pollutant",
            "sensor_type": "chemical",
            "unit": "AQI",
        },
        "co": {
            "name": "CO",
            "type": "pollutant",
            "sensor_type": "chemical",
            "unit": "AQI",
        },
        "t": {
            "name": "Temperature",
            "type": "weather",
            "sensor_type": "meteorological",
            "unit": "°C",
        },
        "p": {
            "name": "Pressure",
            "type": "weather",
            "sensor_type": "meteorological",
            "unit": "hPa",
        },
        "h": {
            "name": "Humidity",
            "type": "weather",
            "sensor_type": "meteorological",
            "unit": "%",
        },
        "w": {
            "name": "Wind",
            "type": "weather",
            "sensor_type": "meteorological",
            "unit": "m/s",
        },
    }

    filtered_data = []

    for key, meta in sensor_meta.items():
        if key in iaqi:
            filtered_data.append(
                {
                    "type": meta["type"],
                    "name": meta["name"],
                    "value": iaqi[key]["v"],
                    "unit": meta["unit"],
                    "sensor_type": meta["sensor_type"],
                    "timestamp": timestamp,
                }
            )

    return filtered_data


# https://docs.openaq.org/about/about
# https://aqicn.org/api/ru/
