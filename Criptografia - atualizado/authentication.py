import sqlite3
import database as db
import utils as u
import hashutils as hu
import config

def verify_user_exist(user_input):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = ?", (user_input,))
    temp = cursor.fetchone()
    if temp: username = temp[0]; cursor.close(); conn.close(); return username
    else: cursor.close(); conn.close(); return None

def verify_if_is_admin(user_id):
    conn = db.get_connection()
    cursor = conn.cursor ()
    cursor.execute("SELECT username FROM users WHERE id = ? AND admin = 1", (user_id,)) 
    temp = cursor.fetchone()
    if temp: cursor.close(); conn.close(); return True
    else: cursor.close(); conn.close(); return None



def password_authentication(user_id, password_input, salt, PEPPER, password_hash):
    attempt_hash = hu.text_to_hash(hu.text_plus_salt_and_pepper(password_input, salt, PEPPER))

    if attempt_hash == db.get_password_hash(user_id): return True
    else: return False

    


    
    
        

    

    





    
    

    