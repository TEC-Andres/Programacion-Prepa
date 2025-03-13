'''
#       Sesión 13: Assignment 13
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   12/03/2024
#       Última Modificación:      13/03/2024
'''
import pandas as pd
import os 
from lib.color import FG, Style

class Main:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'Alumnos.xlsx')
        self.df = pd.read_excel(self.file_path)
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Iniciando el programa.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Visualizando el siguiente archivo {FG.H00AA00 + os.path.basename(self.file_path) + FG.RESET}.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Para ver la lista de comandos, escriba help en la consola.{FG.RESET + Style.RESET_ALL}")

    def lista(self):
        students = self.df.iloc[1:, 3].dropna().tolist()
        return "\n".join([f"{i+1}.- {student}" for i, student in enumerate(students)])

    def correo(self):
        ids = self.df.iloc[1:, 1].dropna().astype(str).tolist()
        emails = [i + "@tec.mx" for i in ids]
        return "\n".join([f"{i+1}.- {email}" for i, email in enumerate(emails)])

    def carrera(self, person):
        row = self.df[self.df.iloc[:, 3] == person]
        if row.empty:
            return "No se halló a la persona"
        return f"{person} quiere estudiar {row.iloc[0, 5]}"

    def asistencia(self, person):
        row = self.df[self.df.iloc[:, 3] == person]
        if row.empty:
            return "No se halló a la persona"
        total = len(self.df.columns) - 4
        attended = (row.iloc[0, 4:] == "X").sum()
        percentage = (attended / total) * 100 if total > 0 else 0
        return f"{person} tiene un porcentaje de asistencia del {percentage:.2f}%"

    def get_ids(self):
        ids = self.df.iloc[1:, 1].dropna().tolist()
        return "\n".join([f"{i+1}.- {id}" for i, id in enumerate(ids)])
    
    def clear(self):
        os.system('cls')
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Visualizando el siguiente archivo {FG.H00AA00 + os.path.basename(self.file_path) + FG.RESET}.{FG.RESET + Style.RESET_ALL}")
        return ""
    
    def errorMessage(self, message):
        print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} {message}{FG.RESET + Style.RESET_ALL}")
        return ""


    def help(self):
        return f"""{Style.BRIGHT + FG.H5555FF}Lista de comandos{FG.RESET + Style.RESET_ALL}
    asistencia <nombre> -   Muestra el porcentaje de asistencia de un alumno
    carrera <nombre>    -   Muestra la carrera de un alumno
    cls    -   Limpia la consola
    correo  -   Muestra los correos de los alumnos
    exit    -   Sale del programa
    help    -   Muestra esta lista de comandos
    ID    -   Muestra la lista de IDs de los alumnos
    lista   -   Muestra la lista de alumnos
    """

if __name__ == "__main__":
    main = Main()
    while True:
        cmd = input(">>> ")
        if cmd == "exit":
            break
        parts = cmd.split()
        commands = {
            "lista": main.lista,
            "correo": main.correo,
            "carrera": lambda: main.carrera(parts[1]) if len(parts) == 2 else main.errorMessage("Error de sintaxis"),
            "asistencia": lambda: main.asistencia(parts[1]) if len(parts) == 2 else main.errorMessage("Error de sintaxis"),
            "ID": main.get_ids,
            "help": main.help,
            "cls": main.clear
        }
        if not parts:
            continue
        action = commands.get(parts[0], lambda: main.errorMessage("El comando que escribiste no existe, checa la ortofragía y vuelve a intentar"))
        print(action())
