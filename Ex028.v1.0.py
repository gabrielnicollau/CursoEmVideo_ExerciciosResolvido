"""
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
"""

from random import randint  # Módulo para gerar número inteiro aleatório.

computador = randint(0, 5)  # Fazer o computador gerar um número aleatório.
print(computador)
print('=-' * 20)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar...')
print('=-' * 20)

jogador = int(input('Em que número eu pensei ? '))  # Escolha do jogador.

if jogador == computador:
    print('\033[32mPARABÉNS!\033[m Você acertou!')

else:
    print('\033[31mVOCÊ PERDEU!\033[m O computador pensou no número \033[32m{}\033[m e não no \033[31m{}\033[m.'.format(computador, jogador))
