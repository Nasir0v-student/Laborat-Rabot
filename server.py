from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, text, bindparam
import json

# Строка подключения к базе данных MySQL
connection_string = "mysql+pymysql://kostya:daniil123!@192.168.50.127:3306/calculator+"
# Создание объекта engine для работы с базой данных
engine = create_engine(connection_string, echo=True)

# Инициализация Flask приложения
app = Flask(__name__)
# Включение CORS для всех маршрутов, начинающихся с /api/
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Главная страница
@app.route("/")
def index():
    return "Hello world"

# Получение всех пользователей
@app.route("/api/user/all")
def get_products():
    with engine.connect() as connection:
        # Выполнение SQL-запроса для получения всех записей из таблицы
        raw_result = connection.execute(text("SELECT * FROM `calculator+`"))
        result = []
        # Преобразование результата в список словарей
        for r in raw_result.all():
            result.append(r._asdict())
        return jsonify(result)

# Добавление нового пользователя
@app.route("/api/user", methods=["POST"])
def add_product():
    if request.method == "POST":
        form = request.form  # Получение данных из формы
        with engine.connect() as connection:
            # SQL-запрос для вставки нового пользователя
            query = text("INSERT INTO `calculator+` (Nickname, Email, Password) VALUES (:Nickname, :Email, :Password) returning *")
            # Привязка параметров к запросу
            query = query.bindparams(bindparam("Nickname", form.get("Nickname")))
            query = query.bindparams(bindparam("Email", form.get("Email")))
            query = query.bindparams(bindparam("Password", form.get("Password")))
            result = connection.execute(query)  # Выполнение запроса
            connection.commit()  # Подтверждение транзакции
            return jsonify(result.fetchone()._asdict())  # Возврат добавленного пользователя
    return jsonify({"message": "Error"})  # Возврат ошибки, если метод не POST

# Удаление пользователя по ID
@app.route("/api/user/<id>", methods=["DELETE"])
def delete_user(id):
    if request.method == "DELETE":
        with engine.connect() as connection:
            # SQL-запрос для удаления пользователя
            query = text("DELETE FROM `calculator+` WHERE id = :id;")
            query = query.bindparams(bindparam("id", id))  # Привязка ID пользователя
            result = connection.execute(query)  # Выполнение запроса
            connection.commit()  # Подтверждение транзакции
            return jsonify({"message": "success", "id": id})  # Возврат сообщения об успехе
    return jsonify({"message": "Error"})  # Возврат ошибки, если метод не DELETE

# Получение, обновление или удаление пользователя по ID
@app.route("/api/user/<id>", methods=["GET", "DELETE", "PUT"])
def user(id: int):
    if request.method == "PUT": 
        with engine.connect() as connection:
            # SQL-запрос для обновления данных пользователя
            query = text("UPDATE user SET Nickname = :Nickname, Email = :Email, Password = :Password WHERE id = :id")
            # Привязка параметров к запросу
            query = query.bindparams(bindparam("Nickname", request.form.get("Nickname")))
            query = query.bindparams(bindparam("Email", request.form.get("Email")))
            query = query.bindparams(bindparam("Password", request.form.get("Password")))
            query = query.bindparams(bindparam("id", id))  # Привязка ID пользователя
            result = connection.execute(query)  # Выполнение запроса
            connection.commit()  # Подтверждение транзакции
            
            # Получение обновленных данных пользователя
            query = text("SELECT * FROM user WHERE id = :id")
            query = query.bindparams(bindparam("id", id))
            result = connection.execute(query)
            return jsonify(result.fetchone()._asdict())  # Возврат обновленного пользователя
        return jsonify({"message": "Error"})  # Возврат ошибки, если что-то пошло не так

# Запуск приложения
def main():
    app.run("localhost", 8000, debug=True)

if __name__ == "__main__":
    main()  # Запуск функции main, если файл выполняется как основной
