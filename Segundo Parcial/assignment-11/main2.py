'''
#       Sesión 11: Assignment 11.2
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main2.py
#
#       Creado:                   24/02/2024
#       Última Modificación:      26/02/2024
'''
import os

class Path():
    def __init__(self):
        pass

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def abrir(self, file_path, cantidad_de_filas=10):
        base_dir = os.path.join(os.path.dirname(__file__), 'db')
        full_path = os.path.join(base_dir, file_path)
        if not os.path.exists(full_path):
            print(f"El archivo {full_path} no existe.")
            return

        try:
            with open(full_path, 'r') as file:
                content = file.readlines()
                total_filas = len(content)
                header = content[0]  # Get the header row
                i = 1  # Start from the first data row
                while True:
                    self.clear_screen()
                    print(header)  # Print the header row
                    print(''.join(content[i:i+cantidad_de_filas]))
                    if i + cantidad_de_filas < total_filas:
                        user_input = input("Presiona  'a' para agregar una nueva fila, 'e' para editar, 'i' para ir al numero de fila, 'b' para regresar, o 'enter' para reiniciar:\n>>> ")
                        if user_input.lower() == 'a':
                            nueva_fila = content[-1].strip().split('|')
                            nueva_fila[0] = str(int(nueva_fila[0]) + 1)
                            nueva_fila = '   |'.join(nueva_fila)
                            self.agregar_fila(file_path, nueva_fila)
                            with open(full_path, 'r') as file:
                                content[:] = file.readlines()
                        elif user_input.lower() == 'e':
                            self.columna_edit(file_path, content)
                        elif user_input.lower() == 'i':
                            fila = int(input("Pon el número de fila:\n>>> "))
                            i = fila
                        elif user_input.lower() == 'b':
                            i = max(1, i - cantidad_de_filas)  # Ensure we don't go before the first data row
                        else:
                            i += cantidad_de_filas
                            if i >= total_filas:
                                i = 1  # Reset to the first data row
                    else:
                        user_input = input("Fin de la base de datos. Presiona 'e' para editar, 'i' para ir al numero de fila, 'b' para regresar, o 'enter' para reiniciar:\n>>> ")
                        if user_input.lower() == 'e':
                            self.columna_edit(file_path, content)
                        elif user_input.lower() == 'i':
                            fila = int(input("Pon el número de fila:\n>>> "))
                            i = fila
                        elif user_input.lower() == 'b':
                            i = max(1, i - cantidad_de_filas)  # Ensure we don't go before the first data row
                        else:
                            i = 1  # Reset to the first data row
        except Exception as e:
            print(f"An error occurred: {e}")

    def columna_edit(self, file_path, content):
        fila = int(input("Pon el número de columna: "))
        new_value = input("Pon el nuevo valor: ")
        self.editar(file_path, fila, new_value)
        base_dir = os.path.join(os.path.dirname(__file__), 'db')
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, 'r') as file:
            content[:] = file.readlines()

    def editar(self, file_path, fila, new_value):
        base_dir = os.path.join(os.path.dirname(__file__), 'db')
        full_path = os.path.join(base_dir, file_path)
        if not os.path.exists(full_path):
            print(f"El archivo {full_path} no existe.")
            return

        try:
            with open(full_path, 'r') as file:
                content = file.readlines()
            
            if fila < len(content):
                columnas = content[fila].strip().split('|')
                if len(columnas) >= 3:
                    columnas[2] = "   " + new_value
                    content[fila] = '|'.join(columnas) + '\n'
                    with open(full_path, 'w') as file:
                        file.writelines(content)
                    print(f"Columna {fila} actualizada con exito.")
                else:
                    print(f"La comulmna {fila} no cuenta con suficientes filas.")
            else:
                print(f"La columna {fila} no existe.")
        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            with open(full_path, 'r') as file:
                content = file.readlines()
            
            if fila < len(content):
                print(content[fila])
            else:
                print(f"Row {fila} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def agregar_fila(self, file_path, nueva_fila):
        base_dir = os.path.join(os.path.dirname(__file__), 'db')
        full_path = os.path.join(base_dir, file_path)
        if not os.path.exists(full_path):
            print(f"The file {full_path} does not exist.")
            return
        try:
            with open(full_path, 'r') as file:
                content = file.readlines()
                first_row = content[0].strip().split('|')
                last_row = content[-1].strip().split('|')
                new_index = str(int(last_row[0].strip()) + 1)  # Calculate the new index
            
            columnas = nueva_fila.split('|')
            if len(columnas) < 3:
                print("Un error sucedio, no hay suficientes filas'|'.")
                return
            columnas[0] = f'{new_index}   '  # Set the new index
            columnas[1] = input("Pon la cantidad de personas maximas que pueden usar la mesa\n>>> ")
            columnas[1] = f'   {columnas[1]}             '
            columnas[2] = input("¿La mesa esta disponible? (Si/No)\n>>> ")
            columnas[2] = f'   {columnas[2]}'

            nueva_fila = '|'.join(columnas)
            with open(full_path, 'a') as file:
                file.write('\n'+ nueva_fila)
            print("Nueva fila agregada con exito.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = Path()
    while True:
        file_path = input("Pon la base de datos (localizada en /db/) que quieras acceder: ")
        path.abrir(file_path)