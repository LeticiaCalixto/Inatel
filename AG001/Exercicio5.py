from sympy import *

# DEFINE x E y COMO VARIAVEIS SIMBOLICAS
var('x y')

# CALCULO DO c
matricula = 1582
c = matricula % 10

# PRIMEIRA EQUACAO
a = exp(x-3) + exp(x-1) + exp(x) - (c + 1)

# SEGUNDA EQUACAO
b = x**4 - 4*x**3 + 3*x - c

# TERCEIRA EQUACAO
c1 = 4*sin((c + 1)*x) + 2

print('Exercicio 5:')

print('\n    Resultado da primeira equacao: ', solve(a))

print('\n    Resultado da segunda equacao:  ', solve(b))

print('\n    Resultado da terceira equação: ', solve(c1))