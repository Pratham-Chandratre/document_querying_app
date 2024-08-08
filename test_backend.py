from cryptography.fernet import Fernet
import sqlite3
from cryptography.fernet import Fernet
from backend import authenticate

# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher = Fernet(key)

def test_encryption_decryption():
    password = "testpass"
    encrypted_password = cipher.encrypt(password.encode()).decode()
    decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()

    print(f"Original password: {password}")
    print(f"Encrypted password: {encrypted_password}")
    print(f"Decrypted password: {decrypted_password}")

    assert password == decrypted_password, "Encryption/Decryption failed!"

if __name__ == "__main__":
    test_encryption_decryption()



# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher = Fernet(key)

def test_authentication():
    username = "testuser"
    password = "testpass"

    # Clean up any previous test data
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()

    # Register a new user
    encrypted_password = cipher.encrypt(password.encode()).decode()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, encrypted_password))
    conn.commit()
    conn.close()

    # Test authentication
    assert authenticate(username, password), "Authentication failed!"

if __name__ == "__main__":
    test_authentication()
