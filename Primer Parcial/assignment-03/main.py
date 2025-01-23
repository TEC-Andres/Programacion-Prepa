'''
#       Sesión 3: Assignment-03
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Descripción de la actividad:
#       Esta actividad se trata de usar los diferentes tipos
#       de datos en Python.
#
#       Creado:                   16/01/2024
#       Última Modificación:      20/01/2024
'''

'''
PROMPT DE CHATGPT: Dame diez ejercicios de diferentes dificultades para aprender a usar el if en python

Respuesta por CHATGPT:
¡Claro! Aquí tienes 10 ejercicios de diferentes niveles de dificultad para practicar el uso de if en Python:

A.- Ejercicios Básicos
1.- Número par o impar
Escribe un programa que solicite un número al usuario y determine si es par o impar.
Ejemplo de entrada: 7
Ejemplo de salida: El número es impar.

2.- Edad mínima para conducir
Pide al usuario su edad y dile si tiene la edad mínima para conducir (18 años).
Ejemplo de entrada: 16
Ejemplo de salida: No puedes conducir.

3.- Mayor de dos números
Solicita dos números al usuario y muestra cuál es mayor.
Ejemplo de entrada: 3 y 5
Ejemplo de salida: El número mayor es 5.

4.- Positivo, negativo o cero
Pide al usuario que introduzca un número y dile si es positivo, negativo o cero.
Ejemplo de entrada: -4
Ejemplo de salida: El número es negativo.

B.- Ejercicios Intermedios
5.- Descuento en una tienda
Si un cliente gasta más de $100, recibe un 10% de descuento. Escribe un programa que calcule el precio final.
Ejemplo de entrada: $120
Ejemplo de salida: Precio final: $108.

6.- Número dentro de un rango
Pide un número al usuario y verifica si está entre 10 y 50 (incluidos).
Ejemplo de entrada: 25
Ejemplo de salida: El número está dentro del rango.

7.- Validación de contraseña
Crea un programa que verifique si una contraseña ingresada por el usuario coincide con una contraseña guardada (por ejemplo, "python123").
Ejemplo de entrada: python123
Ejemplo de salida: Acceso concedido.

8.- Juego de adivinar un número
Define un número secreto (por ejemplo, 7). Pide al usuario que adivine el número e indica si acertó o no.
Ejemplo de entrada: 5
Ejemplo de salida: Incorrecto. Inténtalo de nuevo.

C.- Ejercicios Avanzados
9.- Clasificación de notas
Escribe un programa que convierta una calificación numérica en una letra según la escala:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Menor a 60
Ejemplo de entrada: 85
Ejemplo de salida: Tu calificación es B.

10.- Año bisiesto
Solicita un año al usuario y determina si es bisiesto. (Un año es bisiesto si es divisible entre 4, pero no entre 100, salvo que también sea divisible entre 400).
Ejemplo de entrada: 2000
Ejemplo de salida: El año es bisiesto.

¿Quieres ayuda con alguno de estos ejercicios? 😊
'''
# SRC
import hashlib
import random

class excersice: 
    def __init__(self): 
        pass

    def __P1(self):
        __a1 = int(input("Pon un número: "))
        if (__a1 % 2) == 0:
            print(f"El número {__a1} es par.\n")
        else:
            print(f"El numero {__a1} es non.\n")

    def __P2(self):
        __b2 = int(input("Pon tu edad para acceder al bar: "))
        if(__b2 < 18):
            print("No tienes la edad para pasar\n")
        else:
            print("Tienes la edad suficiente para pasar\n")

    def __P3(self):
        __a3 = int(input("Define tu primer número: "))
        __b3 = int(input("Define tu primer número: "))

        if(__a3 < __b3):
            print(f"{__b3} es el número mayor\n")
        else:
            print(f"{__a3} es el número mayor\n")
        pass

    def __P4(self):
        __a4 = int(input("Define algún numero: "))
        if(__a4 <  0):
            print(f"{__a4} es menor que cero\n")
        elif(__a4 > 0):
            print(f"{__a4} es mayor que cero\n")
        else:
            print(f"{__a4} es cero\n")
        pass
    
    def __P5(self):
        __a5 = int(input("Precio de un producto: $"))
        print(f"Precio original: ${__a5}")
        print(f"Precio con 10% de descuento: ${__a5 * 0.9}\n")
        pass

    def __P6(self):
        __a6 = int(input("¿Está el número dentro del rango? (Rango entre 0 al 50): "))
        if (__a6 >= 0 ) & (__a6 <= 50):
            print(f"{__a6} está dentro del rango.\n")
        else:
            print(f"{__a6} está fuera del rango.\n")
        pass

    def __P7(self):
        __a7 = str(input("Pon tu contraseña: "))
        __b7 = "ca8f60b2cc7f05837d98b208b57fb6481553fc5f1219d59618fd025002a66f5c" # Contraseña: Hola mundo
        __a7 = hashlib.sha256(__a7.encode()).hexdigest()

        if(__a7 == __b7):
            print("Acceso Concedido\n")
        else:
            print("Acceso Denegado\n")
        pass

    def __P8(self):
        __a8 = int(input("Pon un número del 1 al 3: "))
        __b8 = random.randint(1, 3)

        if (__a8 == __b8):
            print(f"¡Enhorabuena! El número era {__b8}\n")
        else:
            print(f"¡Oh no! El número correcto era {__b8}\n")
        pass

    def __P9(self):
        __a9 = int(input("Pon la nota que sacaste en el curso: "))
        if (__a9 >= 90) & (__a9 <= 100):
            print("Tu nota es una 'A'\n")
        elif (__a9 >= 80) & (__a9 <= 89):
            print("Tu nota es una 'B'\n")
        elif (__a9 >= 70) & (__a9 <= 79):
            print("Tu nota es una 'C'\n")
        elif (__a9 >= 60) & (__a9 <= 69):
            print("Tu nota es una 'D'\n")
        elif (__a9 < 60):
            print("Tu nota es una 'F'\n")
        else:
            print("Coloca una nota del 0 al 100\n")
        pass

    def __P10(self):
        __a10 = int(input("Pon algún año para checar si es bisiesto: "))
        if (__a10 % 4 == 0 and __a10 % 100 != 0) or (__a10 % 400 == 0):
            print("Este año fue bisiesto\n")
        else:
            print("Este año no fue bisiesto\n")
        pass 

    def index(self):
        __index = int(input("Pon el número del ejercicio (del 1 al 10): "))
        __list = [self.__P1, self.__P2, self.__P3, self.__P4, self.__P5, self.__P6, self.__P7, self.__P8, self.__P9, self.__P10]
        if 1 <= __index <= len(__list):
            __list[__index - 1]()
        else:
            print("Índice fuera de rango\n")

if __name__ == "__main__":
    excersice = excersice()
    while True:
        excersice.index()