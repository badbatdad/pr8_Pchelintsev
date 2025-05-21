import random
import string

def generate_password(length=10):
<<<<<<< HEAD
    # Алфавит: строчные + заглавные буквы
    alphabet = string.ascii_letters
=======
    # Алфавит: строчные, заглавные, цифры и спецсимволы
    alphabet = string.ascii_letters + string.digits + string.punctuation
>>>>>>> dev
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

print("Пример пароля:", generate_password())
