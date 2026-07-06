from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend Running",
        "status": "success"
    })

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({
            "success": True,
            "message": "Login Successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid Username or Password"
    }), 401


if __name__ == "__main__":
    app.run(debug=True)