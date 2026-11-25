import sqlite3
import config

DATABASE_NAME = "users.db"

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   salt TEXT NOT NULL,
                   password_hash TEXT NOT NULL,
                   admin INTEGER NOT NULL DEFAULT 0 CHECK(admin IN (0, 1))

);
""")
    conn.commit()
    cursor.close()
    conn.close()

def add_user(username, salt, password_hash):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
INSERT INTO users (username, salt, password_hash)
                   VALUES (?, ?, ?)
                
""", (username, salt, password_hash))
    conn.commit()
    cursor.close()
    conn.close()

def remove_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
DELETE FROM users WHERE username = ?
                
""", (username,))
    conn.commit()
    cursor.close()
    conn.close()   

def get_user_id(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = cursor.fetchone()
    if user_id is None: cursor.close(); conn.close(); return None
    cursor.close()
    conn.close()
    return user_id[0]

def get_salt(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT salt FROM users WHERE id = ?", (user_id,))
    salt = cursor.fetchone()
    if salt is None: cursor.close(); conn.close();return None
    cursor.close()
    conn.close()
    return salt[0]

def get_password_hash(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE id = ?", (user_id,))
    real_hash = cursor.fetchone()
    cursor.close()
    conn.close()
    return real_hash[0]

def get_PEPPER():
    PEPPER = config.PEPPER
    return PEPPER

def give_admin(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET admin = 1 WHERE id = ?", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
def remove_admin(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET admin = 0 WHERE id = ?", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()




