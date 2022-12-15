"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""

número = int(input('Digite um número para saber o seu fatorial: '))
contador = número  # Contador vai recer o número
resultado = 1  # Multiplicador a partir do 1

while contador > 0:  # Enquanto contador(número) for maior que 0
    resultado *= contador  # resultado vai receber o resultado * contador, ou seja, número * 1.
    contador -= 1  # Em cada loop o contador vai tirar 1, número - 1

print('O fatorial de {} é {}.'.format(número, resultado))