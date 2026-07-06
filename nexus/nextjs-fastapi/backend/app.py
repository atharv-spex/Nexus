from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    username: str
    password: str

@app.get("/")
def home():
    return {
        "message": "FastAPI Backend Running",
        "status": "success"
    }

@app.post("/login")
def login(data: LoginData):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (data.username, data.password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return {
            "success": True,
            "message": "Login Successful"
        }

    return {
        "success": False,
        "message": "Invalid Username or Password"
    }