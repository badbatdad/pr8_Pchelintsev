import random
import string

def generate_password(length=10):
    # Алфавит: строчные + заглавные буквы
    alphabet = string.ascii_letters
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

print("Пример пароля:", generate_password())
