# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

print('''Escolha uma opção: 
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')

# COMPUTADOR:

lista = (['Pedra', 'Papel', 'Tesoura'])
escolha_pc = choice(lista)

print('A escolha foi {}'.format(escolha_pc))

# JOGADOR:

escolha_jogador = str(input('Qual é a sua escolha: ')).lower()






