import tabulate
import clipboard
from passwords import encrypt, decrypt
from cryptography.fernet import Fernet


class PasswordManagerFile:
    
    def __init__(self):
        pass
    
    def _gen_key(self, path: str = './key.txt'):
        with open(path, 'wb') as f:
            key = Fernet.generate_key()
            f.write(key)
        
    def _set_key(self, path: str = './key.txt', key: str = '-'):
        with open(path, 'w') as f:
            f.write(key)
    
    def _get_key(self, path: str = './key.txt') -> str:
        with open(path, 'r') as f:
            key = f.read()
            return key
    
    def get_last_id(self) -> int:
        with open('./passwords.txt', 'r') as f:
            lines = f.readlines()
        last_id = 0
        for line in lines:
            if line.split(',')[0].isnumeric():
                last_id = max(int(line.split(',')[0]), last_id)
        return last_id
    
    def add(self, username, password, website) -> None:
        new_password = encrypt(password, self._get_key()).decode()
        with open('./passwords.txt', 'a') as f:
            f.write(f"{self.get_last_id() + 1},{username},{new_password},{website}\n")
                    
    def list(self) -> list[tuple[str, str, str, str]]:
        with open('./passwords.txt', 'r') as f:
            lines = f.readlines()
        table = []
        for line in lines:
            table.append(line.split(','))
        return table

    def print(self) -> None:
        table = self.list()
        for row in table:
            if row == ['\n']:
                continue
            row[2] = '*' * 8
        print(tabulate.tabulate(table, headers=["Username", "Password", "Website"]))
        print()
        
    def delete(self, id) -> None:
        with open('./passwords.txt', 'r') as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            if line == ['\n']:
                continue
            if int(line.split(',')[0]) != id:
                new_lines.append(line)
        with open('./passwords.txt', 'w') as f:
            f.writelines(new_lines)
            
    def edit(self, id, new_password) -> None:
        with open('./passwords.txt', 'r') as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            if line.split(',')[0] == str(id):
                np = encrypt(new_password, self._get_key()).decode()
                new_lines.append(f"{id},{line.split(',')[1]},{np},{line.split(',')[3]}\n")
            else:
                new_lines.append(line)
        with open('./passwords.txt', 'w') as f:
            f.writelines(new_lines)
            
    def get(self, id):
        with open('./passwords.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.split(',')[0] == str(id):
                hashed_password = line.split(',')[2]
                pswd = decrypt(hashed_password, self._get_key())
                clipboard.copy(pswd)
                