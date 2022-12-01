"""Exercício Python 49: refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que
utilizando agora  um laço for."""

numero = int(input('Digite o número para saber a sua tabuada: '))
print('\033[33m=-\033[m' * 8)

for tabuada in range(0, 11):
    calculo = numero * tabuada
    print('{} x {:2} = {}'.format(numero, tabuada, calculo))

print('\033[33m=-\033[m' * 8)
print('\033[31mFIM!\033[m')
