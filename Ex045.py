# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('''Escolha uma opção: 
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')

# Informações computador e jogador:

escolha_pc = randint(0, 2)  # Computador escolhe 1 número entre 1 e 3.

escolha_jogador = int(input('Digite a sua opção:  '))  # Jogador digita um número entre 1 e 3.

if escolha_jogador <= 2:  # Opção de escolhas do 0 ao 2, maior que isso parar o programa.

    print('\033[32mVAMOS COMEÇA!\033[m')
    print('=-' * 20)
    print('JO')
    sleep(1.0)
    print('KEN')
    sleep(1.0)
    print('PÔ')
    print('=-' * 20)
    print(escolha_pc)
    # 1° COMPUTADOR ESCOLHEU PEDRA
    if escolha_pc == 0:  # Computador jogou Pedra.
        if escolha_pc == escolha_jogador:  # Jogador escolheu (Pedra). Pedra x Pedra: Empate.
            print('\033[33mEMPATE!\033[m')

        elif escolha_jogador == 1:  # Jogador escolheu (Papel). Pedra x Papel: Papel.
            print('Computador jogou Pedra e você jogou Papel.')
            print('\033[32mVOCÊ GANHOU!\033[m')

        elif escolha_jogador == 2:  # Jogador escolheu (Tesoura). Pedra x Tesoura: Pedra
            print('O computador jogou Pedra e você jogou Tesoura.')
            print('\033[37mO COMPUTADOR GANHOU!\033[m')

    # 2° COMPUTADOR ESCOLHEU PAPEL
    elif escolha_pc == 1:  # Computador jogou Papel.
        if escolha_pc == escolha_jogador:  # Jogador escolheu (Papel). Papel x Papel: Empate.
            print('O computador jogou Papel e você jogou Papel.')
            print('\033[33mEMPATE!\033[m')

        elif escolha_jogador == 0:  # Jogador escolheu (Pedra). Papel x Pedra: Papel.
            print('O computador jogou Papel e você jogou Pedra.')
            print('\033[37mCOMPUTADOR GANHOU!\033[m')

        elif escolha_jogador == 2:  # Jogador escolheu (Tesoura). Papel x Tesoura: Tesoura.
            print('O computador jogou Papel e você jogou Tesoura.')
            print('\033[32mVOCÊ GANHOU!\033[m')

    # 3° COMPUTADOR ESCOLHEU TESOURA
    elif escolha_pc == 2:  # Computador jogou tesoura.
        if escolha_pc == escolha_jogador:  # Jogador escolheu (tesoura). Tesoura x Tesoura: Empate.
            print('O computador jogou Tesoura e você jogou Tesoura.')
            print('\033[33mEMPATE!\033[m')

        elif escolha_pc == 0:  # Jogador escolheu (Pedra). Tesoura x Pedra: Pedra.
            print('O computador jogou Tesoura e você jogou Pedra.')
            print('\033[32mVOCÊ GANHOU!\033[m')

        elif escolha_jogador == 1:  # Jogador escolheu (Papel). Tesoura x Papel: Papel.
            print('O computador jogou Tesoura e você jogou Papel.')
            print('\033[37mCOMPUTADOR GANHOU!\033[m')
else:
    print('\033[31mOPÇÃO INVÁLIDA, ESCOLHA UMA OPÇÃO DE 0 A 2.\033[m')
