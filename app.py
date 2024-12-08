from flask import Flask, render_template, request
from API import get_weather_data, get_location_key
from manager import check_bad_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_results = None
    error_message = None

    if request.method == 'POST':
        start_city = request.form.get('start_city')
        end_city = request.form.get('end_city')

        if not start_city or not end_city:
            error_message = "Пожалуйста, укажите оба города."
        else:
            try:
                start_location_key = get_location_key(start_city)
                end_location_key = get_location_key(end_city)

                start_weather = get_weather_data(start_location_key)
                end_weather = get_weather_data(end_location_key)

                start_bad_weather = check_bad_weather(*start_weather)
                end_bad_weather = check_bad_weather(*end_weather)

                weather_results = {
                    "start": {
                        "city": start_city,
                        "temperature": start_weather[0],
                        "wind_speed": start_weather[1],
                        "rain_probability": start_weather[2],
                        "bad_weather": start_bad_weather,
                    },
                    "end": {
                        "city": end_city,
                        "temperature": end_weather[0],
                        "wind_speed": end_weather[1],
                        "rain_probability": end_weather[2],
                        "bad_weather": end_bad_weather,
                    },
                }
            except Exception as e:
                error_message = str(e)

    return render_template('index.html', weather_results=weather_results, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
