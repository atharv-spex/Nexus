from database.db import Database


class AuthService:

    @staticmethod
    def login(username, password):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        return user