import random
import string
import time

def generate_email():
    # Добавляем миллисекундный штамп для гарантированной уникальности
    timestamp = int(time.time() * 1000)
    return f"roman_setrakov_46_{timestamp}@yandex.ru"

def generate_password():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))

def generate_short_password():
    return ''.join(random.choice(string.ascii_letters) for _ in range(5))

def generate_name():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(6))
