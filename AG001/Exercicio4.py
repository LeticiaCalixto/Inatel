from numpy import *

# CALCULO DO c
matricula = 1582
c = matricula % 10

# CALCULANDO AS FONTES DO CIRCUITO
v1 = 10 + (2*c)
v2 = 5 + (2*c)

# CALCULANDO O SISTEMA DE EQUACOES
M1 = matrix([
[35,-10],
[-10,30]
])

M2 = matrix([
[v1],
[-v2]
])

M1_Inv = linalg.inv(M1)
x = M1_Inv * M2

# ATRIBUINDO OS VALORES DAS CORRENTES
i1 = x[0,0]
i2 = x[1,0]
i3 = -(i1 + i2)

print('Exercicio 4:')

print('\n  Resultado do sistema de equações:')
print(x)

print('\n   Corrente I1 = ', round(i1, 3), 'A')

print('\n   Corrente I2 = ', round(i2, 3),'A')

print('\n   Corrente I3 = ', round(i3, 3),'A')