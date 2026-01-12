from hashlib import sha256
from os import urandom
from config import PEPPER

def text_to_hash(text):
    
    hashed_text = sha256(text).hexdigest()
    return hashed_text

def generate_salt(n): #n = numero de bytes ex: 16, 32 ou 64
    random_bytes = urandom(n)
    hex_string =  "".join(f"{byte:02x}" for byte in random_bytes)
    return hex_string

def text_plus_salt_and_pepper(text, salt, PEPPER):
    tempered_text = (text + salt + PEPPER).encode()
    return tempered_text

def create_password_hash(user_input, salt, PEPPER):
    hash = text_to_hash(text_plus_salt_and_pepper(user_input, salt, PEPPER))
    return hash



