'''
#       Sesión 5: Assignment-05
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Descripción de la actividad:
#       Esta actividad se trata de aprender a usar
#       ciclos
#
#       Creado:                   27/01/2024
#       Última Modificación:      27/01/2024
'''
'''
PROMPT DE CHATGPT: Generame diez problemas usando python que usen el while

Respuesta por CHATGPT:
Aquí tienes diez problemas que utilizan while en Python, organizados por dificultad creciente:

Básico
Cuenta regresiva
Escribe un programa que pida al usuario un número entero positivo y luego haga una cuenta regresiva hasta 0 usando while.

Suma de números ingresados
Pide al usuario que ingrese números enteros positivos. La entrada termina cuando el usuario ingresa un número negativo, y el programa debe imprimir la suma total de los números ingresados.

Número adivinado
Genera un número aleatorio entre 1 y 10. Luego, pide al usuario que adivine el número hasta que lo acierte, mostrando mensajes de "más alto" o "más bajo" según corresponda.

Intermedio
Suma de dígitos
Pide al usuario un número entero y usa while para calcular la suma de sus dígitos.

Verificación de contraseña
Define una contraseña y pide al usuario que la ingrese hasta que coincida con la contraseña correcta.

División por restas sucesivas
Pide dos números enteros positivos 
𝐴
A y 
𝐵
B, y usa restas sucesivas en un while para calcular 
𝐴
/
𝐵
A/B sin usar / ni //.

Avanzado
Número de Fibonacci más cercano
Pide un número 
𝑁
N al usuario y encuentra el número de Fibonacci más cercano usando un while.

Verificación de número primo
Pide un número y usa while para verificar si es primo, es decir, que solo sea divisible por 1 y por sí mismo.

Invertir un número
Pide un número entero y usa while para invertir sus dígitos.

Secuencia de Collatz
Pide un número al usuario y genera su secuencia de Collatz usando while:

Si el número es par, se divide entre 2.
Si es impar, se multiplica por 3 y se le suma 1.
Se repite hasta llegar a 1.
Si quieres que implemente alguno en código, dime cuál te interesa más. 🚀
'''
import time
import random
import hashlib

class excersice: 
    def __init__(self): 
        pass

    # 1. Cuenta regresiva
    # Escribe un programa que pida al usuario un número entero positivo y luego haga una cuenta regresiva hasta 0 usando while.
    def __P1(self):
        __a1 = int(input("Cuenta regresiva: "))
        while __a1 >= 0:
            print(__a1)
            time.sleep(1)
            __a1 -= 1

    # 2. Suma de números ingresados
    # Pide al usuario que ingrese números enteros positivos. La entrada termina cuando el usuario ingresa un número negativo, y el programa debe imprimir la suma total de los números ingresados.
    def __P2(self):
        __a2 = 0
        while True:
            __b2 = int(input("Escribe un número: "))
            if __b2 < 0:
                break
            __a2 += __b2

        print(__a2)
        pass

    # 3. Número adivinado
    # Genera un número aleatorio entre 1 y 10. Luego, pide al usuario que adivine el número hasta que lo acierte, mostrando mensajes de "más alto" o "más bajo" según corresponda.
    def __P3(self):
        __a3 = random.randint(1, 10)
        while True:
            __b3 = int(input("Adivina el número: "))
            if __b3 == __a3:
                print("¡Correcto!")
                break
            elif __b3 < __a3:
                print("Más alto")
            else:
                print("Más bajo")
        print(__a3)

    # 4. Suma de dígitos
    # Pide al usuario un número entero y usa while para calcular la suma de sus dígitos.
    def __P4(self):
        __a4 = int(input("Escribe un número: "))
        __b4 = 0
        while __a4 > 0:
            __b4 += __a4 % 10
            __a4 //= 10
        print(__b4)
        pass

    # 5. Verificación de contraseña
    # Define una contraseña y pide al usuario que la ingrese hasta que coincida con la contraseña correcta.
    def __P5(self):
        __a5 = str(input("Pon tu contraseña: "))
        __b5 = "ca8f60b2cc7f05837d98b208b57fb6481553fc5f1219d59618fd025002a66f5c" # Contraseña: Hola mundo
        __a5 = hashlib.sha256(__a5.encode()).hexdigest()

        while __a5 != __b5:
            __a5 = str(input("Contraseña incorrecta, intenta de nuevo: "))
            __a5 = hashlib.sha256(__a5.encode()).hexdigest()
        else:
            print("Contraseña correcta\n")
        pass

    # 6. División por restas sucesivas
    # Pide dos números enteros positivos A y B, y usa restas sucesivas en un while para calcular A/B sin usar / ni //.
    def __P6(self):
        __a6 = int(input("Define A: "))
        __b6 = int(input("Define B: "))
        __c6 = 0
        while __a6 >= __b6:
            __a6 -= __b6
            __c6 += 1
        print(f"A/B = {__c6}")
        pass

    # 7. Número de Fibonacci más cercano
    # Pide un número N al usuario y encuentra el número de Fibonacci más cercano usando un while.
    def __P7(self):
        __a7 = int(input("Escribe un número: "))
        __b7 = 0
        __c7 = 1
        while __c7 < __a7:
            __b7, __c7 = __c7, __b7 + __c7
        print(f"El número de Fibonacci más cercano es {__c7 if __c7 - __a7 < __a7 - __b7 else __b7}") # No entendí como se hace esto (usé chatgpt)
        pass

    # 8. Verificación de número primo
    # Pide un número y usa while para verificar si es primo, es decir, que solo sea divisible por 1 y por sí mismo.
    # NOTA: se que la complejidad del algoritmo es O(n^2), así que para números grandes se tarda demasiado en encontrar si es primo o no
    def __P8(self):
        __a8 = int(input("Escribe un número: "))
        while True:
            for i in range(2, __a8):
                if __a8 % i == 0:
                    print(f"{__a8} no es un número primo")
                    break
            else:
                print(f"{__a8} es un número primo")
            break
        pass

    # 9. Invertir un número
    # Pide un número entero y usa while para invertir sus dígitos.
    def __P9(self):
        __a9 = int(input("Escribe un número: "))
        __b9 = 0
        while __a9 > 0:
            __b9 = __b9 * 10 + __a9 % 10
            __a9 //= 10
        print(__b9)
        pass

    # 10. Secuencia de Collatz
    # Pide un número al usuario y genera su secuencia de Collatz usando while: (si es un número non, se multiplica por 3 y se suma 1, pero si es par, divide el número entre 2)
    def __P10(self):
        __a10 = int(input("Escribe un número: "))
        while __a10 != 1:
            if __a10 % 2 == 0:
                __a10 //= 2
            else:
                __a10 = __a10 * 3 + 1
            print(__a10)
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