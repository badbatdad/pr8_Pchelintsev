import random
import string

def generate_password(length=10):
    # Базовый алфавит: строчные буквы
    alphabet = string.ascii_lowercase
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

print("Пример пароля:", generate_password())
