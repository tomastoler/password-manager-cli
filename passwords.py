from cryptography.fernet import Fernet
from string import ascii_letters, digits
from random import randint

chars = ascii_letters + digits + "!#$%&/()=?¡¿~`^,.-;:_<|°¬>"

def encrypt(password: str, key: str) -> bytes:
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt(password, key) -> str:
    f = Fernet(key)
    return f.decrypt(password).decode()

def generate_password(lenght: int = 16) -> str:
    return ''.join(chars[randint(0, len(chars))] for _ in range(lenght))