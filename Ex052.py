"""Exercício Python 52: faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

seunumero = int(input('Digite um número inteiro para saber se ele é \33[32mprimo\033[m ou \033[31mnão\033[m: '))

contador = 0  # contador
for divisor in range(2, seunumero + 1):
    if seunumero % divisor == 0:  # números primos tem o resto igual a 1, apenas resto zero divisivel por 1 e ele mesmo.
        contador = contador + 1

if contador == 0:  # Se o contador não achar nenhum número igual a zero, ele é primo
    print('O número digitado foi \033[32m{}\033[m, \033[32mÉ PRIMO!\033[m'.format(seunumero))

else:
    print('O número digitado foi \033[32m{}\033[m, \033[31mNÃO É PRIMO!\033[m'.format(seunumero))
