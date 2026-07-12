from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Flask Backend Running",
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
    })


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data["username"]
    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    if user:
        conn.close()
        return jsonify({
            "success": False,
            "message": "Username already exists"
        })

    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Registration Successful"
    })


if __name__ == "__main__":
    app.run(debug=True)