# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('''Escolha uma opção: 
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA''')

# Informações computador e jogador:

escolha_pc = randint(1, 3)  # Computador escolhe 1 número entre 1 e 3.

escolha_jogador = int(input('Digite a sua opção:  '))  # Jogador digita um número entre 1 e 3.
if escolha_jogador <= 3:
    print('\033[32mVAMOS COMEÇA!\033[m')
    print('=-' * 20)
    print('JO')
    sleep(1.0)
    print('KEN')
    sleep(1.0)
    print('PÔ')
    print('=-' * 20)


    if escolha_pc == 1:  # Computador jogou Pedra:

        if escolha_jogador == escolha_pc:  # Pedra x Pedra: Empate.
            print('Computador jogou Pedra e você jogou Pedra.')
            print('EMPATE!')

        elif escolha_jogador == 2:  # Pedra x Papel: Papel ganha.
            print('Computador jogou Pedra e você jogou Papel.')
            print('JOGADOR GANHOU!')

        elif escolha_jogador == 3:  # Pedra x Tesoura: Pedra ganha.
            print('Computador jogou Pedra e você jogou Tesoura')
            print('COMPUTADOR GANHOU!')


        elif escolha_pc == 2:  # Computador jogou Papel:
            if escolha_jogador == escolha_pc:  # Papel x Papel: Empate.
                print('Computador jogou Papel e você jogou Papel.')
                print('EMPATE!')

        elif escolha_jogador == 1:  # Papel x Pedra: Papel ganha.
            print('Computador jogou Papel e você jogou Pedra.')
            print('COMPUTADOR VENCEU!')

        elif escolha_jogador == 3:  # Papel x Tesoura: Tesoura ganha.
            print('Computador jogou Papel e você jogou Tesoura.')
            print('JOGADOR GANHOU')

        elif escolha_pc == 3:  # Computador jogou Tesoura:
            if escolha_jogador == escolha_pc:  # Tesoura x Tesoura: Empate.
                print('Computador jogou Tesoura e você jogou Tesoura.')
                print('EMPATE!')

        elif escolha_jogador == 1:  # Tesoura x Pedra: Pedra ganha.
            print('Computador jogou Tesoura e você jogou Pedra.')
            print('JOGADOR GANHOU!')

        elif escolha_jogador == 2:  # Tesoura x papel: Tesoura ganha.
            print('Computador jogou Tesoura e você jogou Papel')
            print('COMPUTADOR GANHOU!')

else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')
