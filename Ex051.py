"""Exercício Python 61: refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while."""


print('=-' * 12)
print('\033[33mOS 10 PRIMEIROS TERMOS DE UMA PA\033[m')
print('=-' * 12)

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
limite = 1  # Limite começa com um para fazer os 10 primeiros termos, se fosse zero seria 11.

while limite <= 10:  # ‘Loop’ vai até 10.
    print('{} -> '.format(termo), end='')  # Mostrar o primeiro termo.
    termo += razão  # o termo será somada a razão em cada loop, ou seja, vai aumentando o valor em cada volta.
    limite += 1  # Limite do loop.
