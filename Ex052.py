"""Exercício Python 52: faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

seunúmero = int(input('Digite um número inteiro pra saber se ele é primo ou não: '))

contador = 0
for divisor in range(2, seunúmero):
    if seunúmero % divisor == 0:
        contador = contador + 1



if contador == 0:
    print('O número digitado foi \033[32m{}\033[m, \033[32mÉ PRIMO!\033[m'.format(seunúmero))

else:
    print('O número digitado foi\033[32m{}\033[m, \033[31mNÃO É PRIMO!\033[m'.format(seunúmero))