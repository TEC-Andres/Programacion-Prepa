'''
#       Sesión 14: Proyecto Parcial 2
#       Fernando Chávez Nolasco ─ A01284698
#       Andrés Rodríguez Cantú ─ A01287002
#       Roberto André Guevara Martínez ─ A01287324
#       Víctor Manuel Sánchez Chávez ─ A01287522
#       
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: lib/commands.py
#
#       Creado:                   13/03/2024
#       Última Modificación:      14/03/2024
'''
import os
import sys
from lib.color import FG, Style, checkInfo

class Dict(dict):
    mensajes_ayuda = {
        'ayuda': {
            'description': 'Muestra la lista de comandos disponibles.',
            'syntax': 'ayuda [-descripcion|-sintaxis]'
        },
        'cls': {
            'description': 'Limpia la consola.',
            'syntax': 'cls'
        },
        'db': {
            'description': 'Muestra el archivo actual.',
            'syntax': 'db'
        },
        'exit': {
            'description': 'Cierra el programa.',
            'syntax': 'exit'
        },
        'libro': {
            'description': 'Reserva/Devuelve un libro',
            'syntax': 'libro [reservar|devolver] <nombre_libro>'
        }
    }

class cmd:
    def __init__(self):
        pass

    def init(self):
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Iniciando el programa.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Para ver la lista de comandos, escriba 'ayuda' en la consola.{FG.RESET + Style.RESET_ALL}")

    def ayuda(self, *args):
        if not args:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Use 'ayuda -descripcion' o 'ayuda -sintaxis' para más detalles.{FG.RESET + Style.RESET_ALL}")
            return

        if '-descripcion' in args:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Descripciones de comandos:{FG.RESET + Style.RESET_ALL}")
            for command, info in Dict.mensajes_ayuda.items():
                print(f"	{checkInfo(command, FG.H00AAAA)}{FG.RESET + FG.H443A3B}	―{FG.RESET + Style.RESET_ALL} {info['description']}")

        elif '-sintaxis' in args:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Sintaxis de comandos:{FG.RESET + Style.RESET_ALL}")
            for command, info in Dict.mensajes_ayuda.items():
                print(f"	{checkInfo(command, FG.H00AAAA)}{FG.RESET + FG.H443A3B}	―{FG.RESET + Style.RESET_ALL} {info['syntax']}")

        else:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Opción inválida. Use '-descripcion' o '-sintaxis'.{FG.RESET + Style.RESET_ALL}")

    def salir(self):
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Programa cerrado con éxito.{FG.RESET + Style.RESET_ALL}")
        sys.exit()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
