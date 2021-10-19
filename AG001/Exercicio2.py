from sympy import *

# DEFINE s E t COMO VARIAVEIS SIMBOLICAS
var('s t')

# CALCULO DO c
matricula = 1582
c = matricula % 10

# EQUAÇÃO POSICAO
s = (((-t**3) / 3) + 2*t**2 - c)

# EQUACAO VELOCIDADE, COM T IGUAL A 3
a = diff(s, t).subs(t,3)

# EQUACAO ACELERACAO, COM T IGUAL A 5
b = diff(diff(s, t), t).subs(t,5)

print('Exercicio 2: ')

print('\n  Equacao da velocidade com t = 3: ')
print('         Velocidade = ',a," m/s.")

print('\n  Equacao da acelaracao com t = 5: ')
print('         Aceleracao = ',b," m/s².")