'''
#       Sesión 14: Proyecto Parcial 2
#       Andrés Rodríguez Cantú ─ A01287002
#       Roberto André Guevara Martínez ─ A01287324
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   13/03/2024
#       Última Modificación:      13/03/2024
'''
import os
from lib.commands import Cmd as cmd
import pandas as pd

class Main:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'db\\books.xlsx')
        self.df = pd.read_excel(self.file_path)
        cmd.init(self)

if __name__ == "__main__":
    main = Main()
    while True:
        comando = input(">> ")
        try:
            parts = comando.split()
            comando_name = parts[0]
            args = parts[1:]
            getattr(cmd, comando_name)(main, *args)
        except AttributeError:
            print(f"El comando '{comando}' no existe. Favor de revisar la ortografía o checar la lista de comandos con 'help'.")