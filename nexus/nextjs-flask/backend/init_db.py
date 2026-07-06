import sqlite3

# Create (or open) the database
conn = sqlite3.connect("database.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create the users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert a default user
cursor.execute("""
INSERT OR IGNORE INTO users (username, password)
VALUES (?, ?)
""", ("admin", "admin123"))

# Save changes
conn.commit()

# Close the database
conn.close()

print("Database created successfully!")