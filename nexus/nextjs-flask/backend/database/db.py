import sqlite3

class Database:
    @staticmethod
    def connect():
        return sqlite3.connect("database.db")