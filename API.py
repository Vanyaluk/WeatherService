import requests

# Ваш API-ключ от AccuWeather
API_KEY = "19AMmMONydW4JtHKPZ0KcPbdusVdvM3E"
BASE_LOCATION_URL = "http://dataservice.accuweather.com/locations/v1/cities/search"
BASE_FORECAST_URL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"


# Получение ключа местоположения из API
def get_location_key(city):
    params = {"apikey": API_KEY, "q": city}
    response = requests.get(BASE_LOCATION_URL, params=params)
    if response.status_code != 200 or not response.json():
        raise Exception(f"Не удалось найти город: {city}")
    return response.json()[0]["Key"]


def get_weather_data(location_key):
    params = {"apikey": API_KEY, "metric": True}
    response = requests.get(f"{BASE_FORECAST_URL}{location_key}", params=params)

    # Проверяем статус ответа
    if response.status_code != 200:
        raise Exception("Ошибка получения прогноза погоды!")

    try:
        # Получаем JSON-ответ
        forecast = response.json().get("DailyForecasts", [{}])[0]  # Берём первый элемент или пустой словарь

        # Извлекаем значения с безопасным доступом
        temperature = forecast.get("Temperature", {}).get("Maximum", {}).get("Value", "Нет данных")
        wind_speed = forecast.get("Day", {}).get("Wind", {}).get("Speed", {}).get("Value", "Нет данных")
        rain_probability = forecast.get("Day", {}).get("PrecipitationProbability", "Нет данных")

        return temperature, wind_speed, rain_probability

    except Exception as e:
        raise Exception(f"Ошибка обработки данных прогноза: {e}")
