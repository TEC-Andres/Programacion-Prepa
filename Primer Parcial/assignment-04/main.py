'''
#       Sesión 4: Assignment-04
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Descripción de la actividad:
#       Esta actividad se trata de usar ciclos para hacer
#       una prueba Katz
#
#       Creado:                   23/01/2024
#       Última Modificación:      23/01/2024
'''
'''
ACTIVIDADES:

Bañarse
Vestirse
Sanitario
Levantarse
Comidas
Contingencias
'''
# Acividades básicas de la vida diaria
class App:
    continueMsg = "> Pulse cualquier tecla para continuar"

    def __init__(self):
        print("Bienvenido a la prueba de indice de Katz.")
        pass

    def hold(self, func, msg, *args, **kwargs):
        input(f"{msg}")
        if callable(func):
            return func(*args, **kwargs)
        else:
            raise Exception("Function is not callable")

    def choiceToNumber(self, choice):
        if choice == 'A':
            return 1.0
        elif choice == 'B':
            return 0.5
        elif choice == 'C':
            return 0.5
        elif choice == 'D':
            return 0.0

    def begin(self):
        user_name = input("Por favor, ingrese su nombre: ")
        print(f"Hola, {user_name}. Vamos a realizar el siguiente exámen.")
        self.hold(self.sampleQuestion, self.continueMsg)
        pass

    def sampleQuestion(self):
        print("Contesta la siguiente encuesta respondiendo con las letras del inciso A al inciso D con la respuesta que más se identifica.")
        print("Ejemplo: 2+2 es igual a\nA.- 3\nB.- 4\nC.- 5\nD.- 6")
        print("\nSu respuesta: B")
        self.hold(self.Q1, self.continueMsg)
        pass

    def exit(self):
        print("Gracias por participar en la prueba de Katz.")
        pass

    def Q1(self):
        print("Al bañarse ¿Usted recibe alguna ayuda?\n A) No recibo ninguna ayuda\n B)Recibo ayuda en una parte del cuerpo\n C)Recibo ayuda en todo el cuerpo\n D)No me baño")
        while True:
            __Q1 = input("Su respuesta (A, B, C, D): ").upper()
            if __Q1 in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Respuesta inválida. Por favor, ingrese A, B, C o D.")
        self.choiceQ1 = self.choiceToNumber(__Q1)
        self.Q2()
    
    def Q2(self):
        print("¿Necesita ayuda para vestirse?\nA) No recibo ninguna ayuda\n B)Recibo ayuda en una parte del cuerpo\n C)Recibo ayuda en todo el cuerpo\n D)No me visto")
        while True:
            __Q2 = input("Su respuesta (A, B, C, D): ").upper()
            if __Q2 in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Respuesta inválida. Por favor, ingrese A, B, C o D.")
        self.choiceQ2 = self.choiceToNumber(__Q2)
        self.Q3()

    def Q3(self):
        print("¿Necesita ayuda para ir al sanitario?\nA) No recibo ninguna ayuda\n B)Recibo ayuda en una parte del cuerpo\n C)Recibo ayuda en todo el cuerpo\n D)No voy al sanitario")
        while True:
            __Q3 = input("Su respuesta (A, B, C, D): ").upper()
            if __Q3 in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Respuesta inválida. Por favor, ingrese A, B, C o D.")
        self.choiceQ3 = self.choiceToNumber(__Q3)
        self.Q4()
    
    def Q4(self):
        print("¿Necesita ayuda para levantarse?\n A) No recibo ninguna ayuda\n B)Recibo ayuda en una parte del cuerpo\n C)Recibo ayuda en todo el cuerpo\n D)No me levanto")
        while True:
            __Q4 = input("Su respuesta (A, B, C, D): ").upper()
            if __Q4 in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Respuesta inválida. Por favor, ingrese A, B, C o D.")
        self.choiceQ4 = self.choiceToNumber(__Q4)
        self.Q5()

    def Q5(self):
        print("¿Necesita ayuda para comer?\nA) No recibo ninguna ayuda\n B)Recibo ayuda en una parte del cuerpo\n C)Recibo ayuda en todo el cuerpo\n D)No como")
        while True:
            __Q5 = input("Su respuesta (A, B, C, D): ").upper()
            if __Q5 in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Respuesta inválida. Por favor, ingrese A, B, C o D.")
        self.choiceQ5 = self.choiceToNumber(__Q5)
        print(f"Tu puntuación es: {self.choiceQ1 + self.choiceQ2 + self.choiceQ3 + self.choiceQ4 + self.choiceQ5}")
        self.hold(exit, self.continueMsg)
        

if __name__ == "__main__":
    app = App()
    app.begin()