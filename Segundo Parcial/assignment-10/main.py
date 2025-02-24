'''
#       Sesión 10: Assignment 10
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   23/02/2024
#       Última Modificación:      23/02/2024
'''
import math
from scipy.integrate import quad

class funcionesConIntegrales():
    def __init__(self):
        print(
            "Calculadora de funciones con integrales\nFunciones disponibles:\nerf(x), Si(x), Ci(x), Gamma(x), Ei(x)\nLo único que tienes que hacer es escribir el nombre de la función seguido de un paréntesis y el valor de x dentro de él.\nEjemplo: erf(1)\n\nSi quiere poner valores racionales, lo tendra que poner en forma decimal.\n")
        pass

    def erf(self, x):
        # Función en LaTeX: \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^2} dt
        def _integrand(t):
            # La función de error es la integral de 
            return 2/math.sqrt(math.pi) * math.exp(-t**2)
        
        integral, _ = quad(_integrand, 0, x)
        return integral
    
    def Si(self, x): 
        # Función en LaTeX: \int_{0}^{x} \frac{\sin(t)}{t} dt
        def _integrand(t):
            return math.sin(t) / t
        integral, _ = quad(_integrand, 0, x)
        return integral
    
    def Ci(self, x):
        # Función en LaTeX: -\int_{x}^{\infty} \frac{\cos(t)}{t} dt
        def _integrand(t):
            return math.cos(t) / t
        integral, _ = quad(_integrand, x, math.inf)
        return -integral
    
    def Gamma(self, x):
        # Función en LaTeX: \int_{0}^{\infty} t^{x-1} e^{-t} dt
        def _integrand(t):
            return t**(x-1) * math.exp(-t)
        integral, _ = quad(_integrand, 0, math.inf)
        return integral
    
    def Ei(self, x):
        # Función en LaTeX: \gamma + \int_{0}^{x} \frac{-1+e^t}{t} dt - \frac{1}{2}\ln(\frac{1}{x})+\frac{\ln(x)}{2} 
        euler_gamma = 0.57721566490153286060651209008240243104215933593992 # no esta en el modulo math
        def _integrand(t):
            return (-1 + math.exp(t)) / t
        integral, _ = quad(_integrand, 0, x)
        return euler_gamma + integral - 1/2 * math.log(1/x) + math.log(x)/2 

    def execute_function(self, func_call):
        func_name, arg = func_call.split('(')
        arg = float(arg[:-1])  # Quita el paréntesis al final
        if hasattr(self, func_name):
            func = getattr(self, func_name)
            return func(arg)
        else:
            raise AttributeError(f"No se encontro la función '{func_name}'")

if __name__ == "__main__":
    main = funcionesConIntegrales()
    while True:
        func_call = input("Defina el valor de la función: ")
        try:
            result = main.execute_function(func_call)
            print(result)
        except Exception as e:
            print(f"Error: {e}")
