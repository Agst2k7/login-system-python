import hashutils as hu
from time import sleep
import cli
import authentication as ath
import database as db
from config import PEPPER, hash_size
from utils import temp



running = True
step = "menu"
if __name__ == "__main__":
    db.create_table()
    while running:
        if step == "menu":
            user_id = ""
            i = ""
            user = ""
            password_input = ""
            user_input = ""
            cli.menu()
            i = int(input("Escolha uma opção: ").strip())
            if i == 1:
                step = "login"
            if i == 2:
                step = "register"
            if i == 3:
                running = False

#### LOGIN
        if step == "login":
            step = "username_input"
            while step == "username_input":
                user_input = cli.user_input()
                if user_input == "0": step = "menu"; continue
                user = ath.verify_user_exist(user_input)
                if user:
                    step = "password_input"
                    user_id = db.get_user_id(user)
                    while step == "password_input":
                        user_input = cli.password_input(user)
                        if user_input == "0": step = "username_input"; continue
                        proceed = ath.password_authentication(user_id, user_input, db.get_salt(user_id), PEPPER, db.get_password_hash(user_id))
                        if proceed == True:
                            if ath.verify_if_is_admin(user_id) == True:
                                step = "admin_homepage"
                            else: step = "user_homepage"
                            #USER
                            while step == "user_homepage":
                                i = cli.user_home_page(user, user_id)
                                if i.strip() == "exit": step ="menu"; continue
                                else:print("Comando não encontrado."); sleep(1)
                            #ADMIN
                            while step == "admin_homepage":
                                i = cli.admin_home_page(user, user_id)
                                if i == "exit": step = "menu"; continue

                        else:print("Senha inválida."); sleep(3)
                        
                else: print("Usuário não encontrado."); sleep(3)

#### REGISTER
        if step == "register":
            step = "username_input"
            while step == "username_input":
                user_input = cli.create_user_input()
                if user_input == "0": step = "menu"; continue
                temp["username"] = user_input
                step = "password_input"
                while step == "password_input":
                    user_input = cli.create_password_input()
                    temp["salt"] = hu.generate_salt(hash_size)
                    temp["password_hash"] = hu.create_password_hash(user_input, temp["salt"], PEPPER)
                    db.add_user(temp["username"], temp["salt"], temp["password_hash"])
                    print("Usuário criado com êxito."); sleep(2)
                    step = "menu"; continue
                    

                                   

    

        
            
        


    
    
