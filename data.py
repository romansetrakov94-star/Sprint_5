import random
import string

def generate_email():
    """Генерирует уникальный email вида roman_setrakov_46_рандом@yandex.ru"""
    random_digits = random.randint(100, 999)
    return f"roman_setrakov_46_{random_digits}@yandex.ru"

def generate_password():
    """Генерирует пароль из 6 символов (буквы+цифры)"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))

def generate_short_password():
    """Генерирует пароль короче 6 символов (для негативного теста)"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(5))

def generate_name():
    """Генерирует случайное имя (не пустое)"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(6))