import os
import platform

def clear(): # para qualquer plataforma
    os.system("cls" if platform.system() == "Windows" else "clear")

temp = {
    "username": "",
    "salt": "",
    "password_hash": "",
}