from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Пример данных о погоде
weather_data = {
    "Москва": {
        "temperature": "Температура: 20°C",
        "condition": "Состояние: Облачно",
        "humidity": "Влажность: 65%",
        "wind": "Ветер: 5 км/ч"
    },
    "Санкт-Петербург": {
        "temperature": "Температура: 18°C",
        "condition": "Состояние: Дождь",
        "humidity": "Влажность: 80%",
        "wind": "Ветер: 10 км/ч"
    },
    "Новосибирск": {
        "temperature": "Температура: 15°C",
        "condition": "Состояние: Ясно",
        "humidity": "Влажность: 50%",
        "wind": "Ветер: 3 км/ч"
    }
}

@app.route("/")
def index():
    return jsonify({
        "message": "Добро пожаловать в API погоды!",
        "available_cities": list(weather_data.keys())
    })

@app.route("/api/weather/all", methods=["GET"])
def get_all_weather():
    return jsonify(weather_data)

@app.route("/api/weather/<city>", methods=["GET"])
def get_weather(city):
    city_weather = weather_data.get(city)
    if city_weather:
        return jsonify({city: city_weather})
    else:
        return jsonify({"error": "Город не найден"}), 404

@app.route("/api/weather", methods=["POST"])
def calculate():
    data = request.json
    city = data.get("city")
    
    city_weather = weather_data.get(city)
    if city_weather:
        return jsonify({city: city_weather})
    else:
        return jsonify({"error": "Город не найден"}), 404

def main():
    app.run("localhost", 8000, debug=True)

if __name__ == "__main__":
    main()
