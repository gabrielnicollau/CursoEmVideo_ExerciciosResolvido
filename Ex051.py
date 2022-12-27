"""Exercício Python 61: refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while."""


print('=-' * 17)
print('\033[33mOS 10 PRIMEIROS TERMOS DE UMA PA\033[m')
print('=-' * 17)

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

cont = 1

while cont <= 10:
    print('\033[32m{}\033[m \033[34m--> \033[m'.format(termo), end='')
    cont += 1
    termo += razão
print('\033[33mFIM!\033[m')
