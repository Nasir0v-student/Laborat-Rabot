
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, text, bindparam
import json
connection_string = "mysql+pymysql://kostya:daniil123!@192.168.50.127:3306/calculator+"
engine = create_engine(connection_string, echo=True)


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def index():
    return "Hello world"




@app.route("/api/user/all")
def get_products():
    with engine.connect() as connection:
        raw_result = connection.execute(text("SELECT * FROM `calculator+`"))
        result = []
        for r in raw_result.all():
            result.append(r._asdict())
        return jsonify(result)
    return Response(jsonify({"status": "500", "message": "Database is down!"}), status=500)





@app.route("/api/user", methods=["POST"])
def add_product():
    if request.method == "POST":
        form = request.form
        with engine.connect() as connection:
            query = text("INSERT INTO `calculator+` (Nickname, Email, Password) VALUES (:Nickname, :Email, :Password) RETURNING *")
            query = query.bindparams(bindparam("Nickname", form.get("Nickname")))
            query = query.bindparams(bindparam("Email", form.get("Email")))
            query = query.bindparams(bindparam("Password", form.get("Password")))
            result = connection.execute(query)
            connection.commit()
            return jsonify(result.fetchone()._asdict())
        return jsonify({"message": "Error"})





def main():
    app.run("localhost", 8000, debug=True)

if __name__ == "__main__":
    main()
