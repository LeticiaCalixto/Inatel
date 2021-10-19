from sympy import *

# DEFINE x E y COMO VARIAVEIS SIMBOLICAS
var('x y')

# CALCULO DO c
matricula = 1582
c = matricula % 10

# FUNCAO
fx = (x**3 - 4*x**2 + 5*x - c)

# CALCULO DA AREA ENTRE OS INTERVALOS DE 0 E 5
y = integrate(fx, (x, 0, 5))

print('Exercicio 3: ')

print('\n  Area sobre a curva: ',y)