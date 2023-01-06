"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

# Importante programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Cédulas disponíveis de R$50, R$20, R$10 e R$1.

print('=' * 40)
print('{: ^40}'.format(' BANCO GNS '))
print('=' * 40)

# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais

"""
O primeiro passo é tentar empurrar o maior número de notas de 100 reais possível. Como fazemos isso?
Dividindo o valor que o usuário pediu pra sacar por 100.
"""

numero = int(input('Valor para sacar [10-600]: '))

cem = int(numero / 100)
numero = numero % 100

cinquenta = int(numero / 50)
numero = numero % 50

dez = int(numero / 10)
numero = numero % 10

cinco = int(numero / 5)
numero = numero % 5

um = numero

print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
print('Notas R$  1,00 = ', um)