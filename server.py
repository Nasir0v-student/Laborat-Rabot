from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
import json
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    # Возвращаем JSON-ответ с данными из API
    return jsonify({
        "message": "Request1",
        "articles": [
            {
                "Name": "Vasya",
                "description": "2 + 3 = 5",
            },
        ]
    })
    
@app.route("/api/article/all")
def get_article():
    article = [
        {
            "History": "Vasya",
            "description": "2 + 3 = 5",
        },
    ]
    return Response(json.dumps(article), content_type="application/json")
def main():
    app.run("localhost", 8000, debug=True)

if __name__ == "__main__":
    main()
