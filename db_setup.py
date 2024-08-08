import sqlite3
from cryptography.fernet import Fernet

# Generate a key for encryption and save it securely
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Connect to SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY, user_id INTEGER, filename TEXT, content BLOB)''')
c.execute('''CREATE TABLE IF NOT EXISTS queries (id INTEGER PRIMARY KEY, user_id INTEGER, query TEXT, response TEXT)''')

conn.commit()
conn.close()

print("Database setup complete.")
