'''
#       Sesión 14: Proyecto Parcial 2
#       Andrés Rodríguez Cantú ─ A01287002
#       Roberto André Guevara Martínez ─ A01287324
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: lib/inputcolor.py
#
#       Creado:                   13/03/2024
#       Última Modificación:      13/03/2024
'''

from lib.color import FG, Style, checkInfo

class InputColor:
    def __init__(self, color):
        self.color = color