'''
#       Sesión 6: Assignment-06
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Descripción de la actividad:
#       Esta actividad se trata de aprender a usar
#       ciclos, condicionales y el while
#
#       Creado:                   03/02/2024
#       Última Modificación:      03/02/2024
'''
'''
Aquí tienes dos ejercicios que combinan bucles while, for y condicionales en Python:

Ejercicio 1: Adivina el Número (uso de while y condicionales)
Crea un programa que genere un número aleatorio entre 1 y 100. El usuario debe adivinar el número, y después de cada intento, el programa le dirá si su suposición es muy alta, muy baja o correcta. El juego continúa hasta que el usuario adivine el número.

Requisitos:

Usa un bucle while para mantener el juego en funcionamiento hasta que el usuario acierte.
Utiliza condicionales if, elif, y else para verificar las suposiciones.
(Opcional) Muestra cuántos intentos le tomó al usuario adivinar el número.
Ejercicio 2: Pirámide de Asteriscos (uso de for y condicionales)
Crea un programa que pida al usuario un número entero positivo n y luego dibuje una pirámide de asteriscos de n niveles.

Por ejemplo, si el usuario ingresa 4, el programa debería mostrar:

markdown
Copy
Edit
   *
  ***
 *****
*******
Requisitos:

Usa un bucle for para iterar desde 1 hasta n.
Emplea condicionales para controlar la cantidad de espacios y asteriscos en cada línea.
(Opcional) Agrega una condición para que el usuario solo pueda ingresar números positivos.
¿Quieres que te ayude con la solución de alguno?
'''
import random

class exercise:
    def __init__(self):
        pass

    def __P1(self):
        __number = random.randint(1, 100)
        __guess = -1
        __attempts = 0
        while __guess != __number:
            __guess = int(input("Adivina el número [del 1 al 100]: "))
            __attempts += 1
            if __guess < __number:
                print("Muy bajo")
            elif __guess > __number:
                print("Muy alto")
            else:
                print(f"¡Correcto! Te tomó {__attempts} intentos")

    def __P2(self):
        __n = int(input("Ingresa un número positivo: "))
        for i in range(1, __n + 1):
            print(" " * (__n - i) + "*" * (2 * i - 1))

    def index(self):
        __index = int(input("Pon el número del ejercicio (1 o 2): "))
        __list = [self.__P1, self.__P2]
        if 1 <= __index <= len(__list):
            __list[__index - 1]()
        else:
            print("Índice fuera de rango\n")

if __name__ == "__main__":
    excerise = exercise()
    while True:
        excerise.index()