# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

numero = int(input('Digite um número para saber sua tabuada: '))

print('=-' * 7)
print('\033[33mTabuada do {}\033[m'.format(numero))
print('=-' * 7)
print('{} x {:2} = {}'.format(numero, 0, numero * 0))  # Podemos usar os operadores matemáticos dentro do (.format)
print('{} x {:2} = {}'.format(numero, 1, numero * 1))
print('{} x {:2} = {}'.format(numero, 2, numero * 2))
print('{} x {:2} = {}'.format(numero, 3, numero * 3))
print('{} x {:2} = {}'.format(numero, 4, numero * 4))
print('{} x {:2} = {}'.format(numero, 5, numero * 5))
print('{} x {:2} = {}'.format(numero, 6, numero * 6))
print('{} x {:2} = {}'.format(numero, 7, numero * 7))
print('{} x {:2} = {}'.format(numero, 8, numero * 8))
print('{} x {:2} = {}'.format(numero, 9, numero * 9))
print('{} x {:2} = {}'.format(numero, 10, numero * 10))
