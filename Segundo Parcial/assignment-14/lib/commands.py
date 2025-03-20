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
import pandas as pd
from lib.color import FG, Style, checkInfo
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
class Dict(dict):
    mensajes_ayuda = {
        'ayuda': {
            'description': 'Muestra la lista de comandos disponibles.',
            'syntax': 'ayuda [-descripcion|-sintaxis|<str:comando>] '
        },
        'buscar':{
            'description': 'Busca un libro en la base de datos.',
            'syntax': 'buscar <str:nombre_libro>'
        },
        'cls': {
            'description': 'Limpia la consola.',
            'syntax': 'cls'
        },
        'db': {
            'description': 'Imprime a la consola los primeros 10 elementos de la base de datos.',
            'syntax': 'db [int:hoja] [str:base_de_datos]'
        },
        'operacion': {
            'description': 'Reserva/Devuelve un libro',
            'syntax': 'operacion [-reservar|-devolver] <str:nombre_libro>'
        },
        'registro': {
            'description': 'Muestra el registro de rentas.',
            'syntax': 'registro [int:hoja] [str:base_de_datos]'
        },
        'salir': {
            'description': 'Cierra el programa.',
            'syntax': 'salir'
        }
    }

class cmd:
    def __init__(self):
        pass

    def init(self):
        self.file_path_db = os.path.join(os.path.dirname(__file__), os.getenv('PATH_DB'))
        self.file_path_register = os.path.join(os.path.dirname(__file__), os.getenv('PATH_REGISTER'))

        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Iniciando el programa.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Conenctando a la base de datos: {FG.H00AA00 + os.path.basename(self.file_path_db) + FG.RESET}.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Conenctando al registro: {FG.H00AA00 + os.path.basename(self.file_path_register) + FG.RESET}.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Para ver la lista de comandos, escriba 'ayuda' en la consola.{FG.RESET + Style.RESET_ALL}")

    def ayuda(self, *args):
        if not args:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Modulo de ayuda\n{Style.BRIGHT + FG.H0000FF}Para descripciones:{FG.RESET+ Style.RESET_ALL}	Use '{FG.HFFFF00}ayuda {FG.RESET + FG.H848484}-descripcion{FG.RESET + Style.RESET_ALL}' para acceder a las descripciones de los comandos\n{Style.BRIGHT + FG.H0000FF}Para sintaxis:{FG.RESET+ Style.RESET_ALL}		Use '{FG.HFFFF00}ayuda {FG.RESET + FG.H848484}-sintaxis{FG.RESET + Style.RESET_ALL}' para aprender el uso de la sintaxis del programa.{FG.RESET + Style.RESET_ALL}\n{Style.BRIGHT + FG.H0000FF}Para comandos:{FG.RESET+ Style.RESET_ALL}		Use '{FG.HFFFF00}ayuda {FG.RESET + FG.H848484}<comandos>{FG.RESET + Style.RESET_ALL}' para ver el uso junto a la sintaxis de un comando especifico.{FG.RESET + Style.RESET_ALL}")
            return
        
        command = args[0]
        
        if command == '-descripcion':
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Descripciones de comandos:{FG.RESET + Style.RESET_ALL}")
            for cmd, info in Dict.mensajes_ayuda.items():
                print(f"	{checkInfo(cmd, FG.H00AAAA)}{FG.RESET + FG.H443A3B}	―{FG.RESET + Style.RESET_ALL} {info['description']}")
        
        elif command == '-sintaxis':
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Sintaxis de comandos:{FG.RESET + Style.RESET_ALL}")
            for cmd, info in Dict.mensajes_ayuda.items():
                print(f"	{checkInfo(cmd, FG.H00AAAA)}{FG.RESET + FG.H443A3B}	―{FG.RESET + Style.RESET_ALL} {info['syntax']}")
        
        elif command in Dict.mensajes_ayuda:
            print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} {command}:{FG.RESET + Style.RESET_ALL}")
            print(f"	Descripción: {Dict.mensajes_ayuda[command]['description']}")
            print(f"	Sintaxis: {Dict.mensajes_ayuda[command]['syntax']}")
        
        else:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Comando inválido. Use '-descripcion', '-sintaxis' o un comando válido.{FG.RESET + Style.RESET_ALL}")

    def buscar(self, *args):
        path_db=os.getenv('PATH_DB')
        if not args:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Uso incorrecto. Sintaxis: buscar <str:nombre_libro>{FG.RESET + Style.RESET_ALL}")
            return

        book_name = ' '.join(args).strip('\'"')
        try:
            data = pd.read_excel(path_db, sheet_name=None)
            sheet_name = list(data.keys())[0]  # Assuming the first sheet
            df = data[sheet_name]

            # Ensure the book titles are in column B
            if df.columns[1] != 'title':  # Replace 'Book Title' with the actual column name if different
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La columna B no contiene títulos de libros.{FG.RESET + Style.RESET_ALL}")
                return

            # Normalize book_name and column values for comparison
            book_name_normalized = book_name.strip().lower()
            df.iloc[:, 1] = df.iloc[:, 1].str.strip().str.lower()  # Normalize column B (book titles)
            # Check if the book exists in column B
            book_row = df[df.iloc[:, 1].str.contains(book_name_normalized, na=False)]
            if book_row.empty:
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} El libro '{book_name}' no se encuentra en la base de datos.{FG.RESET + Style.RESET_ALL}")
            else:
                book_row = book_row.head(1)  # Get the first match
                print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Información del libro '{book_name}':{FG.RESET + Style.RESET_ALL}")
                print(book_row.to_string(index=False, col_space=15))  # Imprime sin índices con espacio entre columnas
        except Exception as e:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Error al buscar el libro: {str(e)}{FG.RESET + Style.RESET_ALL}")

    def salir(self):
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Programa cerrado con éxito.{FG.RESET + Style.RESET_ALL}")
        sys.exit()

    # db [int:hoja] [str:base_de_datos] hoja referring to the sheet number in the excel file (a.k.a. if it's page 2, it will go from 11 to 20)
    def db(self, *args):
        if len(args) < 1:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Uso incorrecto. Sintaxis: db [int:pagina] [str:base_de_datos]{FG.RESET + Style.RESET_ALL}")
            return

        try:
            page = int(args[0])  # Número de página
            base_de_datos = f"db\\{args[1]}.xlsx" if len(args) > 1 else os.getenv('PATH_DB')

            if not os.path.exists(base_de_datos):
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos '{base_de_datos}' no existe.{FG.RESET + Style.RESET_ALL}")
                return

            try:
                data = pd.read_excel(base_de_datos, sheet_name=None)
                sheet_names = list(data.keys())

                if not sheet_names:
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos no contiene hojas.{FG.RESET + Style.RESET_ALL}")
                    return

                sheet_name = sheet_names[0]
                df = data[sheet_name]
                page_size = 10
                total_rows = len(df)
                total_pages = (total_rows + page_size - 1) // page_size  # Calcular páginas totales

                if page < 1 or page > total_pages:
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Página inválida. Hay {total_pages} páginas disponibles.{FG.RESET + Style.RESET_ALL}")
                    return

                start_row = (page - 1) * page_size
                end_row = min(start_row + page_size, total_rows)  
                print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Mostrando elementos de la página {page} (filas {start_row + 1} a {end_row}) de la hoja '{sheet_name}':{FG.RESET + Style.RESET_ALL}")
                print(df.iloc[start_row:end_row].to_string(index=False, col_space=15))  # Imprime sin índices con espacio entre columnas
            except Exception as e:
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Error al leer la base de datos: {str(e)}{FG.RESET + Style.RESET_ALL}")

        except ValueError:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La página debe ser un número entero.{FG.RESET + Style.RESET_ALL}")

    # operacion [-reservar|-devolver] <str:nombre_libro>
    def operacion(self, *args):
        if len(args) < 2:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Error de sintaxis, recuerda que así se tiene que ver tu comando: operacion [-reservar|-devolver] \"<str:nombre_libro>\"{FG.RESET + Style.RESET_ALL}")
            return

        action = args[0]
        book_name = ' '.join(args[1:]).strip('\'"')  # Strip both single and double quotes

        if action not in ['-reservar', '-devolver']:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Acción inválida. Use '-reservar' o '-devolver'.{FG.RESET + Style.RESET_ALL}")
            return
        
        try:
            # Load the database
            db_path = os.getenv('PATH_DB')
            db_register = os.getenv('PATH_REGISTER')
            if not os.path.exists(db_path):
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos '{db_path}' no existe.{FG.RESET + Style.RESET_ALL}")
                return

            data = pd.read_excel(db_path, sheet_name=None)
            sheet_name = list(data.keys())[0]  # Assuming the first sheet
            df = data[sheet_name]

            # Ensure the book titles are in column B
            if df.columns[1] != 'title':  # Replace 'Book Title' with the actual column name if different
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La columna B no contiene títulos de libros.{FG.RESET + Style.RESET_ALL}")
                return

            # Normalize book_name and column values for comparison
            book_name_normalized = book_name.strip().lower()
            df.iloc[:, 1] = df.iloc[:, 1].str.strip().str.lower()  # Normalize column B (book titles)
            # Check if the book exists in column B
            book_row = df[df.iloc[:, 1].str.contains(book_name_normalized, na=False)]
            if book_row.empty:
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} El libro '{book_name}' no se encuentra en la base de datos.{FG.RESET + Style.RESET_ALL}")
                return
            else:
                book_row = book_row.head(1)  # Get the first match 
            # Perform the action
            status_value = book_row.iloc[0, 4]  # Column E
            if action == '-reservar':
                if status_value != 'Reservado':
                    df.at[book_row.index[0], df.columns[4]] = 'Reservado'
                    print(f"{Style.BRIGHT + FG.H00AA00}[{FG.RESET + FG.H55FF55}ÉXITO{FG.RESET + Style.BRIGHT + FG.H00AA00}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} ¡El libro '{book_name}' ha sido reservado!{FG.RESET + Style.RESET_ALL}")
                else:
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET}El libro '{book_name}' ya está reservado.{Style.RESET_ALL}")
                    return
            elif action == '-devolver':
                if status_value == 'Reservado':
                    df.at[book_row.index[0], df.columns[4]] = 'Disponible'
                    print(f"{Style.BRIGHT + FG.H00AA00}[{FG.RESET + FG.H55FF55}ÉXITO{FG.RESET + Style.BRIGHT + FG.H00AA00}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} ¡El libro '{book_name}' ha sido devuelto!{FG.RESET + Style.RESET_ALL}")
                else:
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET}El libro '{book_name}' no se encuentra reservado.{Style.RESET_ALL}")
                    return
    
            # Save the updated database
            with pd.ExcelWriter(db_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Update the db_register file
            if os.path.exists(db_register):
                register_data = pd.read_excel(db_register)
                new_row = pd.DataFrame({
                    register_data.columns[0]: [register_data.iloc[0, 0] + 1],  # Increment ID
                    register_data.columns[1]: [datetime.now().strftime('%Y-%m-%d %H:%M')],  # Current date
                    register_data.columns[2]: ['Reservacion' if action == '-reservar' else 'Devolucion'],  # Action
                    register_data.columns[3]: [book_name],  # Book title
                    register_data.columns[4]: [book_row.iloc[0, 2]],  # Author
                    register_data.columns[5]: [book_row.iloc[0, 3]]   # Category
                })
                register_data = pd.concat([new_row, register_data], ignore_index=True)
                with pd.ExcelWriter(db_register, engine='openpyxl') as writer:
                    register_data.to_excel(writer, index=False)
            else:
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} El archivo de registro '{db_register}' no existe.{FG.RESET + Style.RESET_ALL}")

        except Exception as e:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Error al procesar la acción: {str(e)}{FG.RESET + Style.RESET_ALL}")

    def registro(self, *args):
        if len(args) < 1:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Uso incorrecto. Sintaxis: registro [int:pagina] [str:base_de_datos]{FG.RESET + Style.RESET_ALL}")
            return

        try:
            page = int(args[0])  # Número de página
            base_de_datos = f"db\\{args[1]}.xlsx" if len(args) > 1 else os.getenv('PATH_REGISTER')

            if not os.path.exists(base_de_datos):
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos '{base_de_datos}' no existe.{FG.RESET + Style.RESET_ALL}")
                return

            try:
                data = pd.read_excel(base_de_datos, sheet_name=None)
                sheet_names = list(data.keys())

                if not sheet_names:
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La base de datos no contiene hojas.{FG.RESET + Style.RESET_ALL}")
                    return

                sheet_name = sheet_names[0]
                df = data[sheet_name]
                page_size = 10
                total_rows = len(df)
                total_pages = (total_rows + page_size - 1) // page_size  # Calcular páginas totales

                if page < 1 or page > total_pages:
                    print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Página inválida. Hay {total_pages} páginas disponibles.{FG.RESET + Style.RESET_ALL}")
                    return

                start_row = (page - 1) * page_size
                end_row = min(start_row + page_size, total_rows)  
                print(f"{Style.BRIGHT + FG.H443A3B}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H443A3B}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Mostrando elementos de la página {page} (filas {start_row + 1} a {end_row}) de la hoja '{sheet_name}':{FG.RESET + Style.RESET_ALL}")
                print(df.iloc[start_row:end_row].to_string(index=False, col_space=15))  # Imprime sin índices con espacio entre columnas
            except Exception as e:
                print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Error al leer la base de datos: {str(e)}{FG.RESET + Style.RESET_ALL}")

        except ValueError:
            print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} La página debe ser un número entero.{FG.RESET + Style.RESET_ALL}")

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
