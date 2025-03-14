'''
#       Sesión 14: Proyecto Parcial 2
#       Fernando Chávez Nolasco ─ A01284698
#       Andrés Rodríguez Cantú ─ A01287002
#       Roberto André Guevara Martínez ─ A01287324
#       Víctor Manuel Sánchez Chávez ─ A01287522
#       
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   13/03/2024
#       Última Modificación:      14/03/2024
'''
import os
from lib.commands import cmd
import pandas as pd
from lib.inputcolor import InputColor

class Main:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'db\\books.xlsx')
        self.df = pd.read_excel(self.file_path)
        cmd.init(self)

if __name__ == "__main__":
    main = Main()
    input_color = InputColor(">> ")
    while True:
        try:
            comando = input_color.start_input().strip()
            if not comando:
                continue
            parts = comando.split()
            comando_name = parts[0]
            args = parts[1:]
            getattr(cmd, comando_name)(main, *args)
        except AttributeError:
            print(f"El comando '{comando}' no existe. Favor de revisar la ortografía o checar la lista de comandos con 'help'.")
        except KeyboardInterrupt:
            print()
            cmd.salir(main)
        except Exception as e:
            print(f"Error: {e}") 