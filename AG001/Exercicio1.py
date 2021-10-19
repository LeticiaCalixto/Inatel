from sympy import *

# DEFINE x E y COMO VARIAVEIS SIMBOLICAS
var('x y')

# CALCULO DO c
matricula = 1582
c = matricula % 10

# EQUACAO A SER USADA NOS CALCULOS DO LIMITE
fx = (3*x**3 - 3) / (4*x**2 - 4)

# LIMITE TENDENDO A 1
a = limit(fx, x, 1) * (c + 1)

# LIMITE TENDENDO A INFINITO
b = limit(fx, x, oo) * (c + 1)

# LIMITE TENDENDO A -INFINITO
c = limit(fx, x, -oo) * (c + 1)

print('Exercicio 1:')

print('\n Limite com x tendendo a 1: ', a)

print('\n Limite com x tendendo a oo: ', b)

print('\n Limite com x tendendo a -oo: ', c)
