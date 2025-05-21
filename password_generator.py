import random
import string

def generate_password(length=10):
    # Алфавит: строчные, заглавные, цифры и спецсимволы
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

print("Пример пароля:", generate_password())
