'''
#       Sesión 7: Proyecto 1er Parcial
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   09/02/2024
#       Última Modificación:      10/02/2024
'''
'''
Proyecto individual para evaluar el 1er Parcial

El objetivo es evaluar los conocimientos adquiridos durante las clases del primer parcial.

Descripción del proyecto:

Realiza una aplicación para la captura de pedidos de un negocio de comida.

La aplicación deberá contener lo siguiente:

    Mensaje de bienvenida al cliente (Dale nombre a tu negocio)
    Solicitud del nombre del cliente
    Menú de cuando menos 5 productos diferentes para realizar un pedido, donde aparezca la opción del producto y su precio (define tu los productos y los precios)
        Una vez que el cliente defina el producto que quiere escoger solicita la cantidad de ese producto que va a querer (Cada vez que escoja el usuario una opción del menú vuelve a mostrar el menu)
        El menú debe de tener una opción para terminar el pedido y una opción para salir del menú,
        Cuando selecciones el usuario seleccioné la opción de terminar el pedido, la aplicación deberá de imprimir el nombre del cliente y un resumen del pedido, con los productos y sus cantidades así como el total.
        En los comentarios del programa es requerido que incluyas el algoritmo que vas a usar para realizar el código

Sé creativo en la forma como despliegas los mensajes al usuario

Lo único que es requerido que valides es que el usuario teclee una opción válida del menú

Recuerda hacer de forma individual el proyecto y no dejes que la IA haga el proyecto por ti.
'''

class Aplicacion:
    def __init__(self):
        print("¡Bienvenid@ a Taco-mer, en donde podras comer los mejores tacos de la ciudad!")
        self.menu = {
            "Taco al pastor": 18.0, "Taco suadero": 15.0, "Tacos de Bistec": 20.0, "Quesadilla": 18.0, "Taco de papa": 15.0, "Refresco": 20.0, "Agua": 15.0
        }
        self.userMenu = {}

    def bienvenida(self):
        input("Pusle cualquier tecla para continuar... ")
        if input != None:
            print("Por favor, ingrese su nombre.")
            self.nombre = input(">>> ")
            self.mostrar_menu()
        pass

    def mostrar_menu(self):
        print(f"Bienvenido, {self.nombre}! Vea aquí el menú de productos con sus respectivos precios:")
        for i, (producto, precio) in enumerate(self.menu.items(), start=1):
            print(f"[{i}] | {producto}: ${precio}")
        print("Por favor, ¿digame qué le gustaría ordernar?")
        self.ordenar()
        pass

    def ordenar(self):
        while True:
            opcion = input(">>> ").strip().lower()
            # Checa por medio de la enumeración de la lista original, si sí esta en la lista, entonces se le asigna a la variable "producto" el valor de la llave del diccionario original.
            if opcion.isdigit() and 1 <= int(opcion) <= len(self.menu):  
                producto = list(self.menu.keys())[int(opcion) - 1]
            # Este método checa el "prompt" del usuario, solo que para evitar que el usuario tenga que definir de manera exacta la opción, se le da la opción de escribirlo en minuscúlas y mayusculas.
            elif opcion in map(str.lower, self.menu.keys()): 
                producto = next(p for p in self.menu.keys() if p.lower() == opcion)
            else:
                print("Por favor, ingrese una opción válida.")
                continue

            print(f"Ha seleccionado: {producto}. ¿Cuánt@s desea ordenar?")
            cantidad = int(input(">>> "))
            if producto in self.userMenu:
                self.userMenu[producto] += cantidad
            else:
                self.userMenu[producto] = cantidad

            print("¿Desea ordenar algo más? [Sí/No]")
            respuesta = input(">>> ").strip().lower()
            # Chequeo para poder cerrar la cuenta
            if respuesta == "no":
                break
            else:
                self.mostrar_menu()
        self.terminar_pedido()
        pass

    def terminar_pedido(self):
        total = 0
        print(f"Su pedido quedará de esta forma {self.nombre}:")
        # Ciclo para poder imprimir los productos y sus respectivas cantidades usando userMenu y los productos almacenados en el. 
        for producto, cantidad in self.userMenu.items():
            precio = self.menu[producto]
            total += precio * cantidad
            print(f"${precio * cantidad}    | {producto} x{cantidad}")
        print(f"Total: ${total}")
        print("Le agradecemos de parte de Taco-mer! ¡Muchas gracias, vuelva pronto!")
        exit()

if __name__ == "__main__":
    app = Aplicacion()
    app.bienvenida()