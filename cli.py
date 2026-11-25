from utils import clear

def menu():
    clear()
    print("="*100)
    print("[1]-ENTRAR\n[2]-CRIAR USUÁRIO\n[3]-SAIR")
    print("="*100)

def user_input():
    clear()
    i = input("Insira o usuário / 0 para cancelar: ").strip()
    return  i

def password_input(username):
    clear()
    print(f"User: {username}")
    i = input("Insira a senha / 0 para cancelar:  ").strip()
    return i

def create_user_input():
    clear()
    i = input("Insira o nome de usuário / 0 para cancelar: ").strip()
    return i

def create_password_input():
    clear()
    i = input("Crie uma senha: / 0 para cancelar: ").strip()
    return i

def user_home_page(username, user_id):
    clear()
    print("="*100)
    print(f"Olá {username}. ID:{user_id}")
    print("="*100)
    print()
    i = input("EXIT para sair: ").strip().lower()
    return i

def admin_home_page(username, user_id):
    clear()
    print("="*100)
    print(f"Olá {username} (admin). ID:{user_id}")
    print("="*100)
    print()
    print("Comandos:")
    print("[1]- Adicionar usuário\n[2]- Remover usuário\n[3]- Adicionar admin\n[4]- Remover admin")
    print()
    i = input("Escolha um comando / EXIT para sair: ").strip().lower()
    return i
