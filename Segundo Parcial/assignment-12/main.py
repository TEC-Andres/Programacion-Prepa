'''
#       Sesión 12: Assignment 12
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   09/03/2024
#       Última Modificación:      09/03/2024
'''
import pandas as pd
import os
from lib.color import FG, Style

class Main(): 
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'college-salaries-sample.xlsx')
        self.df = pd.read_excel(self.file_path)

    def read(self, start, length=10):
        end = start + length
        print(self.df.iloc[start:end])

class InnitText():
    def __init__(self):
        main = Main()
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Iniciando el programa.{FG.RESET + Style.RESET_ALL}")
        file_name = os.path.basename(main.file_path)
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Visualizando el siguiente archivo {FG.H00AA00 + file_name + FG.RESET}.{FG.RESET + Style.RESET_ALL}")

if __name__ == '__main__':
    main = Main()
    InnitText()
    page = 1
    main.read(0)
    while True:
        start = input("¿A qué página iremos?: ")
        if start == '':
            start = page
            page += 1
        elif start.lower() == 'exit':
            print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Finalizando el programa con éxito.{FG.RESET + Style.RESET_ALL}")
            break
        else:
            start = int(start)
            page = start +1
    
        main.read((start - 1) * 10)


