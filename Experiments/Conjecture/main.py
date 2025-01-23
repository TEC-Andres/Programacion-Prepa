from sympy import symbols, integrate, prime
import random

x = symbols('x')
a = 193
b = 149
c = 11
d = 37
e = 29
f = 61

'''a = prime(random.randint(1, 50))  
b = prime(random.randint(1, 50))  
c = prime(random.randint(1, 50))  
d = prime(random.randint(1, 50))  
e = prime(random.randint(1, 50))  
f = prime(random.randint(1, 50))  
'''
integrand = (a*x**2 + b*x + c) / (d*x**2 + e*x + f)
result = integrate(integrand, x)
latex_result = result._repr_latex_()

if __name__ == "__main__":
    print(result)
    print(latex_result)
    print(a,b,c,d,e,f)