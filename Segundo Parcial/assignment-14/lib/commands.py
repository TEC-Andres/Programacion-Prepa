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
#       Última Modificación:      19/03/2024
'''
import os
import sys
from lib.color import FG, Style, checkInfo
import pandas as pd

class Dict(dict):
    mensajes_ayuda = {
        'ayuda': {
            'description': 'Muestra la lista de comandos disponibles.',
            'syntax': 'ayuda [-descripcion|-sintaxis|<comando>] '
        },
        'cls': {
            'description': 'Limpia la consola.',
            'syntax': 'cls'
        },
        'db': {
            'description': 'Imprime a la consola los primeros 10 elementos de la base de datos.',
            'syntax': 'db [str:base_de_datos] [int:hoja]'
        },
        'salir': {
            'description': 'Cierra el programa.',
            'syntax': 'salir'
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
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Conenctando a la base de datos: {FG.H00AA00 + os.path.basename(self.file_path_db) + FG.RESET}.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Conenctando al registro: {FG.H00AA00 + os.path.basename(self.file_path_register) + FG.RESET}.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Para ver la lista de comandos, escriba 'ayuda' en la consola.{FG.RESET + Style.RESET_ALL}")

    def ayuda(self, *args):
        if not args:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Modulo de ayuda\n{Style.BRIGHT + FG.H0000FF}Para descripciones:{FG.RESET+ Style.RESET_ALL}	Use '{FG.HFFFF00}ayuda {FG.RESET + FG.H848484}-descripcion{FG.RESET + Style.RESET_ALL}' para acceder a las descripciones de los comandos\n{Style.BRIGHT + FG.H0000FF}Para sintaxis:{FG.RESET+ Style.RESET_ALL}		Use '{FG.HFFFF00}ayuda {FG.RESET + FG.H848484}-sintaxis{FG.RESET + Style.RESET_ALL}' para aprender el uso de la sintaxis del programa.{FG.RESET + Style.RESET_ALL}\n{Style.BRIGHT + FG.H0000FF}Para comandos:{FG.RESET+ Style.RESET_ALL}		Use '{FG.HFFFF00}ayuda {FG.RESET + FG.H848484}<comandos>{FG.RESET + Style.RESET_ALL}' para ver el uso junto a la sintaxis de un comando especifico.{FG.RESET + Style.RESET_ALL}")
            return

        if '-descripcion' in args:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Descripciones de comandos:{FG.RESET + Style.RESET_ALL}")
            for command, info in Dict.mensajes_ayuda.items():
                print(f"	{checkInfo(command, FG.H00AAAA)}{FG.RESET + FG.H443A3B}	―{FG.RESET + Style.RESET_ALL} {info['description']}")

        elif '-sintaxis' in args:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Sintaxis de comandos:{FG.RESET + Style.RESET_ALL}")
            for command, info in Dict.mensajes_ayuda.items():
                print(f"	{checkInfo(command, FG.H00AAAA)}{FG.RESET + FG.H443A3B}	―{FG.RESET + Style.RESET_ALL} {info['syntax']}")
        elif args[0] in Dict.mensajes_ayuda:
            command = args[0]
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} {command}:{FG.RESET + Style.RESET_ALL}")
            print(f"	Descripción: {Dict.mensajes_ayuda[command]['description']}")
            print(f"	Sintaxis: {Dict.mensajes_ayuda[command]['syntax']}")
        else:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Opción inválida. Use '-descripcion' o '-sintaxis'.{FG.RESET + Style.RESET_ALL}")

    def salir(self):
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Programa cerrado con éxito.{FG.RESET + Style.RESET_ALL}")
        sys.exit()

    # db [str:base_de_datos] [int:hoja] hoja referring to the sheet number in the excel file (a.k.a. if it's page 2, it will go from 11 to 20)
    def db(self, *args):
        #db null null
        if not args: 
            base_de_datos = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db\\books.xlsx')

            if not os.path.exists(base_de_datos):
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos '{base_de_datos}' no existe.{FG.RESET + Style.RESET_ALL}")
                return

            try:
                data = pd.read_excel(base_de_datos, sheet_name=None)
                sheet_names = list(data.keys())

                if not sheet_names:
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos no contiene hojas.{FG.RESET + Style.RESET_ALL}")
                    return

                sheet_name = sheet_names[0]
                df = data[sheet_name]
                print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Mostrando los primeros 10 elementos de la hoja '{sheet_name}':{FG.RESET + Style.RESET_ALL}")
                print(df.head(10))
                return
            except Exception as e:
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Error al leer la base de datos: {str(e)}{FG.RESET + Style.RESET_ALL}")
        
        if len(args) < 2:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Uso incorrecto. Sintaxis: db [int:hoja] [str:base_de_datos]{FG.RESET + Style.RESET_ALL}")
            return

        try:
            hoja = int(args[0])
            base_de_datos = f"db\\{args[1]}.xlsx"

            if not os.path.exists(base_de_datos):
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos '{base_de_datos}' no existe.{FG.RESET + Style.RESET_ALL}")
                return

            try:
                data = pd.read_excel(base_de_datos, sheet_name=None)
                sheet_names = list(data.keys())

                if hoja < 1 or hoja > len(sheet_names):
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Número de hoja inválido. Hay {len(sheet_names)} hojas disponibles.{FG.RESET + Style.RESET_ALL}")
                    return

                sheet_name = sheet_names[hoja - 1]
                df = data[sheet_name]
                print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Mostrando los primeros 10 elementos de la hoja '{sheet_name}':{FG.RESET + Style.RESET_ALL}")
                print(df.head(10))
            except Exception as e:
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Error al leer la base de datos: {str(e)}{FG.RESET + Style.RESET_ALL}")

        except ValueError:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} El número de hoja debe ser un entero.{FG.RESET + Style.RESET_ALL}")


    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
