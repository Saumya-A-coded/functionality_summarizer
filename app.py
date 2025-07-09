from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        data = get_weather_data(city)
        return render_template('index.html', weather=data)
    return render_template('index.html')

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=yourapikey&units=metric"
    response = requests.get(url)
    return response.json()

class WeatherHelper:
    def __init__(self, city):
        self.city = city

    def formatted_output(self, weather_json):
        return {
            "city": self.city,
            "temperature": weather_json["main"]["temp"],
            "description": weather_json["weather"][0]["description"]
        }
