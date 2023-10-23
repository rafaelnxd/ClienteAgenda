import sys
from cx_Freeze import setup, Executable

# Lista de módulos a serem incluídos (pode precisar ser ajustada)
packages = ['packages']


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable('main.py', base=base)]  # Substitua 'seu_script.py' pelo nome do seu script

setup(
    name='AgendaBook',
    version='1.0',
    description='Agenda de Clientes e Produtos',
    options={
        'build_exe': {
            'packages': packages,
        },
    },
    executables=executables
)