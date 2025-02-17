'''
#       Sesión 9: Assignment 9
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   17/02/2024
#       Última Modificación:      17/02/2024
'''
# Lo trabajé solo

class Main():
    def __init__(self):
        self.subjects = {
            "Nombre": "",
            "Edad": "",
            "Correo": "",
            "Teléfono": "",
            "Dirección": ""
            }

    def get_subject_info(self):
        for i in self.subjects:
            self.subjects[i] = input(f"Por favor, ingrese su {i}: ")
        pass

if __name__ == "__main__":
    main = Main()
    main.get_subject_info()
    for i, j in main.subjects.items():
        print(f"Esta es toda la información recuperada:")
        print(f"{i}: {j}")