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
PROMPT DE CHATGPT: Generame diez problemas para usar el for en python con listas y rango

Respuesta por CHATGPT:
¡Claro! Aquí tienes 10 problemas que puedes practicar con el uso de bucles for, listas y range en Python:

1. Sumar los números en un rango
Escribe un programa que sume todos los números del 1 al 100 usando un bucle for y range.
2. Filtrar números pares
Dada una lista de números, usa un bucle for para crear una nueva lista que contenga solo los números pares de la lista original.
python
Copy
Edit
numeros = [1, 4, 7, 10, 13, 16, 19, 22]
3. Factorial de un número
Crea un programa que pida un número al usuario y luego use un bucle for para imprimir el factorial de ese número.
4. Invertir una lista
Dada una lista, utiliza un bucle for y range para invertirla sin usar métodos como .reverse().
python
Copy
Edit
lista = [3, 5, 7, 9]
5. Contar vocales en una palabra
Escribe un programa que pida una palabra y use un bucle for para contar cuántas vocales tiene.
6. Crear una lista de cuadrados
Usa un bucle for y range para crear una lista que contenga los cuadrados de los números del 1 al 10.
7. Eliminar números negativos
Dada una lista de números, usa un bucle for para crear una nueva lista que contenga solo los números no negativos.
python
Copy
Edit
numeros = [-5, 2, -8, 0, 3, 7, -1]
8. Palabras largas
Dada una lista de palabras, usa un bucle for para crear una nueva lista que contenga solo las palabras con más de 5 letras.
python
Copy
Edit
palabras = ["manzana", "sol", "computadora", "casa", "estrella"]
9. Sumar los dígitos de un número
Escribe un programa que pida un número al usuario y use un bucle for para sumar todos sus dígitos.
Ejemplo: Si el usuario introduce 1234, la suma será 10.

10. Reemplazar palabras cortas
Dada una lista de palabras, usa un bucle for para crear una nueva lista en la que las palabras con menos de 4 letras se reemplacen por "corta".
python
Copy
Edit
palabras = ["sol", "estrella", "luz", "paz", "cometa"]

Si necesitas ayuda resolviendo alguno de ellos, ¡puedes avisarme! 😊
'''


class excersice: 
    def __init__(self): 
        pass

    # 1. Sumar los números en un rango
    # Escribe un programa que sume todos los números del 1 al 100 usando un bucle for y range.
    def __P1(self):
        __a1 = int(input("Calcular la suma entre 1 hasta "))
        for i in range(1, __a1 +1):
            __a1 += i
        print(__a1)

    # 2. Filtrar números pares
    # Dada una lista de números, usa un bucle for para crear una nueva lista que contenga solo los números pares de la lista original.
    def __P2(self):
        __a2 = [1, 4, 7, 10, 13, 16, 19, 22]
        __b2 = [i for i in __a2 if i % 2 == 0]
        print(__b2)
        pass

    # 3. Factorial de un número
    # Crea un programa que pida un número al usuario y luego use un bucle for para imprimir el factorial de ese número.
    def __P3(self):
        __a3 = int(input("Calcular el factorial de "))
        for i in range(1, __a3 +1):
            __a3 *= i
        print(__a3)

    # 4. Invertir una lista
    # Dada una lista, utiliza un bucle for y range para invertirla sin usar métodos como .reverse().
    def __P4(self):
        __a4 = [3, 5, 7, 9]
        for i in range(len(__a4)//2):
            __a4[i], __a4[-i-1] = __a4[-i-1], __a4[i]
        print(__a4)
        pass

    # 5. Contar vocales en una palabra
    # Escribe un programa que pida una palabra y use un bucle for para contar cuántas vocales tiene.
    def __P5(self):
        __a5 = input("Escribe una palabra: ")
        __b5 = 0
        for i in __a5:
            if i in __a5:
                __b5 += 1
        print(__b5)
        pass

    # 6. Crear una lista de cuadrados
    # Usa un bucle for y range para crear una lista que contenga los cuadrados de los números del 1 al 10.
    def __P6(self):
        for i in range(1, 11):
            print(f"i^{i}= {i**2}")
        pass

    # 7. Eliminar números negativos
    # Dada una lista de números, usa un bucle for para crear una nueva lista que contenga solo los números no negativos.
    def __P7(self):
        __a7 = [-5, 2, -8, 0, 3, 7, -1]
        for i in __a7:
            if i < 0:
                __a7.remove(i)
        print(__a7)
        pass

    # 8. Palabras largas
    # Dada una lista de palabras, usa un bucle for para crear una nueva lista que contenga solo las palabras con más de 5 letras.
    def __P8(self):
        __a8 = ["manzana", "sol", "computadora", "casa", "estrella"]
        for i in __a8:
            if len(i) <= 5:
                __a8.remove(i)
        print(__a8)
        pass

    # 9. Sumar los dígitos de un número
    # Escribe un programa que pida un número al usuario y use un bucle for para sumar todos sus dígitos.
    def __P9(self):
        __a9 = int(input("Escribe un número: "))
        __b9 = 0
        for i in __a9:
            __b9 += int(i)
        print(__b9)
        pass

    # 10. Reemplazar palabras cortas
    # Dada una lista de palabras, usa un bucle for para crear una nueva lista en la que las palabras con menos de 4 letras se reemplacen por "corta
    def __P10(self):
        __a10 = ["sol", "estrella", "luz", "paz", "cometa"]
        for i in __a10:
            if len(i) < 4:
                __a10[__a10.index(i)] = "corta"
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