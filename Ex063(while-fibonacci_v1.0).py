"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo:"""

print('-' * 23)
print('\033[34mSequência de Fibonacci\033[m')
print('-' * 23)

termo = int(input('aqui: '))

penultimo = 0  # Primeiro valor na sequência de fibonacci.
ultimo = 1  # Segundo valor na sequência de fibonacci.
cont = 3

print('{} --> {}'.format(penultimo, ultimo), end='')

while cont <= termo:
    prox_sequencia = ultimo + penultimo
    print('{} --> '.format(prox_sequencia), end='')

    penultimo = ultimo
    ultimo = prox_sequencia
    cont += 1

print('\033[33mFIM!\033[m')
