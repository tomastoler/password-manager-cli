import os
from pathlib import Path

def get_prefix_os() -> Path:
    if os.name == 'nt':
        return Path('C:/Scripts')
    elif os.name == 'posix':
        return Path().home() / '.local' / 'scripts'
    else:
        raise Exception('OS not suported')