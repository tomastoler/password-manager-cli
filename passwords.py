from cryptography.fernet import Fernet


def encrypt(password: str, key: str) -> bytes:
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt(password, key) -> str:
    f = Fernet(key)
    return f.decrypt(password).decode()